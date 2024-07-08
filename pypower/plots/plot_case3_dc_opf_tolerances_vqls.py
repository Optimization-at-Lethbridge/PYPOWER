import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 8)
objective_classical = [750, 746.252, 746.25, 746.249, 746.25, 746.25, 746.25, 746.25]
feascond_classical = [0.55, 7.65043e-06, 1.2605e-07, 1.72798e-08, 3.73474e-09, 1.2634e-10, 7.45458e-11, 6.57076e-13]
gradcond_classical = [300, 1.91005e-08, 8.32898e-10, 1.62807e-10, 3.35004e-11, 5.89322e-13, 3.22146e-13, 1.24884e-14]
compcond_classical = [5, 3.97907, 0.398269, 0.0398355, 0.00398363, 0.000398364, 3.98364e-05, 3.98364e-06]
costcond_classical = [0, 0.0049905, 2.76671e-06, 1.51793e-07, 6.29565e-08, 6.74017e-10, 7.27857e-10, 1.36104e-10] 

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 3-DC-OPF-VQLS: Iteration vs. Conditions')

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
