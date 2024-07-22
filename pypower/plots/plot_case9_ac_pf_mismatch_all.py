import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 5)
pq_mismatch_classical = [1.630e+00, 1.671e-01, 1.887e-03, 5.714e-07, 5.507e-14]

#vqls-guided
iterations_vqls = range(0, 7)
pq_mismatch_vqls = [1.630e+00, 1.759e-01, 3.673e-03, 2.521e-05, 1.126e-05, 2.033e-08, 6.961e-10]

iterations_hhl = range(0, 6)
pq_mismatch_hhl = [1.630e+00, 1.670e-01, 2.815e-03, 1.929e-05, 2.962e-07, 3.957e-09]

iterations_vqls_preconditioned = range(0, 5)
pq_mismatch_vqls_preconditioned = [1.630e+00, 1.671e-01, 1.887e-03, 5.714e-07, 2.208e-12]

iterations_hhl_preconditioned = range(0, 5)
pq_mismatch_hhl_preconditioned = [1.630e+00, 1.671e-01, 1.887e-03, 5.714e-07, 5.418e-14]

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
plt.title('Case 9-AC-PF: Iteration vs. PQ_Mismatch')
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