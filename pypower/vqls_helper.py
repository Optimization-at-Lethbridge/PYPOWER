import pennylane as qml
from pennylane import numpy as np
#from scipy.sparse import random as sparse_random

class VQLSSolver:
    # Constructor of the VQLSSolver class
    # Initializes the matrix A and vector b along with hyper parameters for the VQLS algorithm.
    # Pads A and b efficiently to the nearest power of 2.
    # Computes the Hermitian matrix H_L used in the cost function.
    def __init__(self, A, b, num_layers=7, max_iterations=220, conv_tol=1e-13, stepsize=0.125):
        self.A = A
        self.b = b
        self.num_layers = num_layers
        self.max_iterations = max_iterations
        self.conv_tol = conv_tol
        self.stepsize = stepsize
        self.original_size = A.shape[0]

        # Pad only the difference to nearest power of 2
        next_pow_of_2 = int(2 ** np.ceil(np.log2(self.original_size)))
        self.padding_size = next_pow_of_2 - self.original_size

        self.padded_A = np.pad(A, ((0, self.padding_size), (0, self.padding_size)), mode='constant')
        self.padded_b = np.pad(b, (0, self.padding_size), mode='constant')

        self.A_dagger = self.padded_A.T.conj()

        b_norm = self.padded_b / np.linalg.norm(self.padded_b)
        P_b = np.outer(b_norm, b_norm)

        I = np.eye(next_pow_of_2)
        self.H_L = self.A_dagger @ (I - P_b) @ self.padded_A
        #print(f"H_L: {self.H_L}")
        #print(f"Norm of H_L: {np.linalg.norm(self.H_L)}")
        self.H_L = self.H_L / np.linalg.norm(self.H_L)

        self.num_qubits = int(np.ceil(np.log2(next_pow_of_2)))
        self.params = self.__initialize_params()

    # Initializes random parameters for the variational quantum circuit.
    def __initialize_params(self):
        params_shape = qml.templates.StronglyEntanglingLayers.shape(n_layers=self.num_layers, n_wires=self.num_qubits)
        return np.random.uniform(low=0, high=2 * np.pi, size=params_shape, requires_grad=True)

    # Defines the variational quantum circuit (ansatz) using the given parameters
    def __ansatz(self, params, wires):
        qml.templates.StronglyEntanglingLayers(params, wires=wires)

    # Defines the cost function that measures the expectation value of the Hermitian matrix H_L
    def __cost_fn(self, params):
        dev = qml.device('default.qubit', wires=self.num_qubits)

        @qml.qnode(dev)
        def qnode(params):
            self.__ansatz(params, wires=range(self.num_qubits))
            H_L_operator = qml.Hermitian(self.H_L, wires=range(self.num_qubits))
            return qml.expval(H_L_operator)

        costs = []  # Track costs for early stopping
        for it in range(self.max_iterations):
            cost = qnode(params)
            costs.append(cost)

            # Early stopping based on cost change (modify threshold as needed)
            if len(costs) > 10 and np.abs(costs[-1] - costs[-10]) < 1e-5:
                break

        return qml.QNode(qnode, dev)  # Return the compiled QNode

    # Optimizes the parameters of the variational quantum circuit using the Adam optimizer
    def __optimize_params(self, cost_fn):
        opt = qml.AdamOptimizer(stepsize=self.stepsize)

        for it in range(self.max_iterations):
            self.params, cost = opt.step_and_cost(cost_fn, self.params)
            #if it % 5 == 0:
            #    print(f" Iteration = {it}, Cost = {cost:.17f}")
            if cost < self.conv_tol:
                break
        #print("Final cost:", cost)
        return self.params

    # Prepares the quantum state using the optimized parameters
    def __prepare_state(self):
        dev = qml.device('default.qubit', wires=self.num_qubits)

        @qml.qnode(dev)
        def qnode(params):
            self.__ansatz(params, wires=range(self.num_qubits))
            return qml.state()

        return qnode(self.params)

    # Extracts the real part of the quantum state vector
    def __extract_solution(self, state):
        return np.real(state[:2 ** self.num_qubits])

    # Adjusts the solution vector to ensure it matches the original problem's dimensions
    def __adjust_solution_vector(self, solution_vector):
        solution_vector /= np.linalg.norm(solution_vector)

        sol = np.dot(self.padded_A, solution_vector)
        coef = np.linalg.norm(self.padded_b) / np.linalg.norm(sol)
        solution_vector *= coef
        solution_vector_final = solution_vector[:self.original_size]
        sol2 = np.dot(self.A, solution_vector_final)

        for i in range(len(solution_vector_final)):
            if np.abs(solution_vector_final[i]) > 0.001:
                if np.abs(sol2[i] - self.b[i]) > np.abs(sol2[i]):
                    solution_vector_final = -solution_vector_final
                break

        return solution_vector_final

    # A public method to solve system of linear equations using variational quantum linear solver hybrid algorithm
    def vqls_solve(self):
        cost_fn = self.__cost_fn(self.params)  # Compile cost function with initial params
        self.params = self.__optimize_params(cost_fn)
        optimal_state = self.__prepare_state()
        solution_vector = self.__extract_solution(optimal_state)
        return self.__adjust_solution_vector(solution_vector)

if __name__ == '__main__':

    def classical_solution(A, b):
        return np.linalg.solve(A, b)

    # Test with a sample matrix
    #np.random.seed(42)
    #A = np.random.rand(16, 16)
    #b = np.random.rand(16)

    # Classical solution
    #c_solution = classical_solution(A, b)

    # Quantum solution
    #For 16 by 16
    #q_solution = vqls(A, b, num_layers=7, max_iterations=290, conv_tol=1e-13, stepsize=0.125)

    #For 8 by 8
    #q_solution = vqls(A, b, num_layers=7, max_iterations=220, conv_tol=1e-13, stepsize=0.125)

    #For 32 by 32
    #q_solution = vqls(A, b, num_layers=7, max_iterations=490, conv_tol=1e-13, stepsize=0.125)

    # Create an instance of the VQLSSolver class
    #vqls_solver = VQLSSolver(A, b, num_layers=7, max_iterations=220, conv_tol=1e-13, stepsize=0.125)

    #For 3 by 3 num_layers=3 max_iterations 250
    #vqls_solver = VQLSSolver(A, b, num_layers=3, max_iterations=250)

    #For 6 by 6 num_layers=3 max_iterations 210
    #vqls_solver = VQLSSolver(A, b, num_layers=3, max_iterations=210)


    #16 by 16
    #vqls_solver = VQLSSolver(A, b, num_layers=7, conv_tol=1e-17, max_iterations=290)

    # Solve the VQLS problem

    # For 14 by 14
    #vqls_solver = VQLSSolver(A, b, num_layers=7, max_iterations=410)

    #q_solution = vqls_solver.vqls_solve()

    # Print classical and quantum solutions
    #print(f"Classical solution: {c_solution}")
    #print(f"Quantum solution: {q_solution}")

    # Calculate the error between classical and quantum solutions
    #error = np.linalg.norm(c_solution - q_solution) / np.linalg.norm(c_solution)
    #print(f"Error between classical and quantum solutions: {error}")


    # Set the random seed for reproducibility
    np.random.seed(42)
    # Generate a 16x16 sparse matrix with a density of 0.23046875 (23.046% non-zero entries)
    #A_sparse = sparse_random(16, 16, density=0.23046875, format='csr', random_state=42)
    #A = A_sparse.toarray()
    # Generate a random vector b of length 16
    A = np.random.rand(16, 16)
    b = np.random.rand(16)
    # Print the sparse matrix A and the vector b
    #print("Sparse matrix A:")
    #print(A_sparse)

    #print("\nVector b:")
    #print(b)

    # Classical solution
    c_solution = np.linalg.solve(A, b)

    # Quantum solution
    # For 16 by 16
    vqls_solver = VQLSSolver(A, b, num_layers=11, conv_tol=1e-17, max_iterations=400) 
    q_solution = vqls_solver.vqls_solve()

    # Print classical and quantum solutions
    print(f"Classical solution: {c_solution}")
    print(f"Quantum solution: {q_solution}")

    # Calculate the error between classical and quantum solutions
    error = np.linalg.norm(c_solution - q_solution) / np.linalg.norm(c_solution)
    print(f"Error between classical and quantum solutions: {error}")
