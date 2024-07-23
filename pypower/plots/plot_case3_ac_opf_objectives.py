import matplotlib.pyplot as plt

iterations_classical = range(0, 11)
objective_classical = [750, 775.00594, 792.88927, 790.13551, 770.24308, 759.21157, 758.89221, 758.24517, 758.20376, 758.20843, 758.21001]

iterations_vqls = range(0, 11)
objective_vqls = [750, 775.00589, 792.88927, 790.13551, 770.24308, 759.21157, 758.89221, 758.24517, 758.20376, 758.20843, 758.21]

plt.figure(figsize=(10, 6))

plt.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color='b', label='Classical Solution')
plt.plot(iterations_vqls, objective_vqls, marker='s', linestyle='--', color='r', label='VQLS (Preconditioned)')

plt.xlabel('Iteration')
plt.ylabel('Objective (Cost)')
plt.title('Case 3-AC-OPF: Iteration vs. Objective (Cost)')
plt.legend()
plt.grid(True)
plt.show()
