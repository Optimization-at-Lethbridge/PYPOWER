import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 4)
pq_mismatch_classical = [4.665e+00, 9.553e-02, 8.368e-05, 6.415e-11]

iterations_vqls = range(0, 4)
pq_mismatch_vqls = [4.665e+00, 9.553e-02, 8.368e-05, 6.851e-11]

iterations_hhl = range(0, 5)
pq_mismatch_hhl = [4.665e+00, 9.598e-02, 6.883e-05, 8.684e-08, 1.077e-10]

iterations_vqls_preconditioned = range(0, 4)
pq_mismatch_vqls_preconditioned = [4.665e+00, 7.522e-02, 5.501e-05, 2.824e-11]

iterations_hhl_preconditioned = range(0, 4)
pq_mismatch_hhl_preconditioned = [4.665e+00, 9.553e-02, 8.368e-05, 6.415e-11]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot each condition with appropriate styles and labels
plt.plot(iterations_classical, pq_mismatch_classical, marker='o', linestyle='-', color=colors[0], label='Classical Solution')
plt.plot(iterations_vqls, pq_mismatch_vqls, marker='s', linestyle='solid', color=colors[1], label='VQLS')
plt.plot(iterations_hhl, pq_mismatch_hhl, marker='^', linestyle='dashed', color=colors[2], label='HHL')
plt.plot(iterations_hhl_preconditioned, pq_mismatch_hhl_preconditioned, marker='D', linestyle='dashdot', color=colors[3], label='HHL_Preconditioned')
plt.plot(iterations_vqls_preconditioned, pq_mismatch_vqls_preconditioned, marker='x', linestyle='dotted', color=colors[4], label='VQLS_Preconditioned')

# Add labels and title
plt.xlabel('Iteration')
plt.ylabel('PQ_Mismatch')
plt.title('Case 5-AC-PF: Iteration vs. PQ_Mismatch')
# Display legend
plt.legend()
# Adjust spacing
plt.subplots_adjust(bottom=0.15)
# Enable grid for better readability
plt.grid(True)
# Set y-axis to logarithmic scale
plt.yscale('log')
# Display the plot
plt.show()