import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 11)
objective_classical = [3901.2551, 2584.3712, 2394.46, 2393.4827, 2395.5364, 2393.3126, 2393.3141, 2393.3144, 2393.3151, 2393.3123, 2393.3126]
feascond_classical = [0.555556, 0.0642908, 3.51269e-05, 4.82097e-08, 0.000888517, 7.52414e-07, 1.31524e-06, 3.55396e-07, 3.3622e-07, 1.93244e-07, 1.19463e-07]
gradcond_classical = [650.075, 0.0105396, 0.000421548, 1.30803e-10,  2.49782e-06, 6.11559e-10, 5.75776e-10, 2.31939e-10, 5.17996e-10, 8.06511e-11, 2.41966e-10]
compcond_classical = [12.4444, 10.7119, 2.7717, 0.342158,  0.0374386, 0.0037223, 0.000372236, 3.72236e-05, 3.72236e-06, 3.72235e-07, 3.72235e-08]
costcond_classical = [0, 0.337467, 0.0734561, 0.000407986, 0.00085766, 0.000927921, 6.24469e-07, 1.42275e-07, 2.85491e-07, 1.15419e-06, 1.30693e-07]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 6ww-DC-OPF-VQLS: Iteration vs. Conditions')

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
