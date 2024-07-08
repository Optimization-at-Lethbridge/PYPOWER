import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 8)
objective_classical = [7278.125, 4133.7108, 4136.7117, 4131.1906, 4131.0246, 4130.9964, 4131.0265, 4131.0264]
feascond_classical = [0.3875, 0.225652, 0.0353576, 0.00869777, 7.31037e-06, 1.38231e-06, 1.13064e-06, 2.01043e-08]
gradcond_classical = [1765, 0.137482, 0.0320064, 3.18998e-06, 1.48806e-09, 2.80858e-11, 2.8715e-12, 7.03037e-13]
compcond_classical = [19.5686, 10.1377, 3.11083, 0.330791, 0.0337898, 0.00337895, 0.000337893, 3.37894e-05]
costcond_classical = [0, 0.431977, 0.000725802, 0.00133436, 4.01646e-05, 6.82348e-06, 7.28796e-06, 1.85092e-08]


# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 9-DC-OPF-VQLS: Iteration vs. Conditions')

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
