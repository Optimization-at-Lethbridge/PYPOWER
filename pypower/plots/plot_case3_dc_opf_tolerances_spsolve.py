import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 9)
objective_classical = [750, 746.25084, 746.25002, 746.25, 746.25, 746.25, 746.25, 746.25, 746.25]
feascond_classical = [0.55, 1.93783e-14, 8.12379e-17, 4.0618e-17, 0, 4.0617e-17, 8.12358e-17, 8.12358e-17, 8.12358e-17]
gradcond_classical = [300, 8.848e-16, 4.95311e-15, 1.00234e-15, 1.88841e-15, 1.16409e-15, 2.5259e-15, 5.9412e-15, 3.31269e-15]
compcond_classical = [5, 3.97906, 0.398261, 0.0398347, 0.00398355, 0.000398356, 3.983e-05, 3.98356e-06, 3.98356e-07]
costcond_classical = [0, 0.00499222, 1.10896e-06, 2.06489e-08, 1.90559e-10, 1.88274e-12, 1.88654e-14, 3.04281e-16, 0]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 3-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')

# Create secondary y-axis for other conditions (logarithmic scale)
ax2 = ax1.twinx()
ax2.plot(iterations_classical, feascond_classical, marker='s', linestyle='solid', color=colors[1], label='Feascond')
ax2.plot(iterations_classical, gradcond_classical, marker='^', linestyle='dashed', color=colors[2], label='Gradcond')
ax2.plot(iterations_classical, compcond_classical, marker='D', linestyle='dashdot', color=colors[3], label='Compcond')
ax2.plot(iterations_classical, costcond_classical, marker='x', linestyle='dotted', color=colors[4], label='Costcond')
ax2.set_yscale('log')
ax2.set_ylabel('Conditions')
ax2.tick_params(axis='y')

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='best')

# Adjust spacing and enable grid for better readability
fig.tight_layout()
ax1.grid(True)

# Display the plot
plt.show()
