import matplotlib.pyplot as plt

iterations_classical = range(0, 11)
gradcond_classical = [0.03, 0.737493,  0.397371, 0.0853692, 0.0619865, 0.0128661, 0.000437377, 0.000184696, 0.000119294, 3.82479e-07, 6.3405e-09]

iterations_vqls = range(0, 11)
gradcond_vqls = [0.03, 0.737498,  0.397383, 0.0853709, 0.0619865, 0.0128661, 0.000437372, 0.000184714, 0.000119291, 1.971849e-06, 6.59292e-09]


plt.figure(figsize=(10, 6))

plt.plot(iterations_classical, gradcond_classical, marker='o', linestyle='-', color='b', label='Classical Solution')
plt.plot(iterations_vqls, gradcond_vqls, marker='s', linestyle='--', color='r', label='VQLS (Preconditioned)')

plt.xlabel('Iteration')
plt.ylabel('Gradcond')
plt.title('Case 3-AC-OPF: Iteration vs. Gradcond')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()