import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 10)
objective_classical = [3901.2551, 2584.3501, 2394.4442, 2393.4827, 2393.3198, 2393.3128, 2393.3125, 2393.3125, 2393.3125, 2393.3125]
feascond_classical = [0.555556, 0.0642891, 1.4045e-14, 5.3408e-16, 1.3324e-16, 8.88181e-17, 4.44089e-17, 4.44089e-17, 4.44089e-17, 4.44089e-17]
gradcond_classical = [650.075, 0.105407, 0.000421522, 2.51256e-15, 3.48091e-15, 6.04277e-15, 4.02243e-15, 2.85459e-15, 1.91308e-15, 6.20741e-15]
compcond_classical = [12.4444, 10.7121, 2.77182, 0.342202, 0.0369565, 0.00370081, 0.000370086, 3.70087e-05, 3.70087e-06, 3.70087e-07]
costcond_classical = [0, 0.337473, 0.0734546, 0.000401405, 6.80397e-05, 2.92638e-06, 9.76409e-08, 9.34946e-09, 9.344455e-10, 9.34412e-11]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 6ww-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')

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
