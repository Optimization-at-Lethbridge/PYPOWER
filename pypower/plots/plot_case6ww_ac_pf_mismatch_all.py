import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 4)
pq_mismatch_classical = [5.061e-01, 1.539e-02, 3.771e-05, 2.086e-10]

iterations_vqls = range(0, 4)
pq_mismatch_vqls = [5.061e-01, 1.539e-02, 3.771e-05, 2.080e-10]

iterations_hhl = range(0, 7)
pq_mismatch_hhl = [5.061e-01, 1.617e-02, 5.419e-04, 1.613e-05, 4.860e-07, 1.433e-08, 4.261e-10]

iterations_vqls_preconditioned = range(0, 4)
pq_mismatch_vqls_preconditioned = [5.061e-01, 1.521e-02, 3.741e-05, 2.068e-10]

iterations_hhl_preconditioned = range(0, 4)
pq_mismatch_hhl_preconditioned = [5.061e-01, 1.539e-02, 3.771e-05, 2.086e-10]

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
plt.title('Case 6ww-AC-PF: Iteration vs. PQ_Mismatch')
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