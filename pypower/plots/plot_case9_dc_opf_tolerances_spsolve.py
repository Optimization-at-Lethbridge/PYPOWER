import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 9)
objective_classical = [7278.125, 4131.0268, 4131.0266, 4131.0266, 4131.0266, 4131.0266, 4131.0266, 4131.0266, 4131.0266]
feascond_classical = [0.3875, 1.54021e-12, 9.18691e-14, 4.4943e-17, 4.4943e-17, 4.4943e-17, 4.4943e-17, 4.4943e-17, 4.4943e-17]
gradcond_classical = [1765, 0.13735, 6.05359e-15, 5.67158e-15, 3.50816e-15, 7.63431e-15, 3.6859e-15, 5.0077e-15, 3.19368e-15]
compcond_classical = [19.5686, 9.7069, 0.970668, 0.0970665, 0.00970665, 0.000970665, 9.70665e-05, 9.70665e-06, 9.70665e-07]
costcond_classical = [0, 0.432346, 3.99544e-08, 2.64865e-10, 2.58474e-12, 2.57527e-14, 2.20109e-16, 0, 2.20109e-16]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 9-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')

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
