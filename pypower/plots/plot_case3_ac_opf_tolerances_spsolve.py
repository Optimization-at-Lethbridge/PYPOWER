import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 11)
objective_classical = [750, 775.00594, 792.88927, 790.13551, 770.24308, 759.21157, 758.89221, 758.24517, 758.20376, 758.20843, 758.21001]
feascond_classical = [0.55, 0.0143651, 7.00967e-05, 1.87073e-06, 0.000138428, 0.000230951, 0.000114532, 0.000708903, 0.000128446, 6.05322e-06,1.11868e-07]
gradcond_classical = [0.03, 0.737493,  0.397371, 0.0853692, 0.0619865, 0.0128661, 0.000437377, 0.000184696, 0.000119294, 3.82479e-07, 6.3405e-09]
compcond_classical = [10, 6.33577, 1.02542, 0.104111, 0.0137429, 0.00194018, 0.000220084, 4.57388e-05, 5.73291e-06, 7.32639e-07, 7.65027e-08]
costcond_classical = [0, 0.00232613, 0.00165971, 0.000255145, 0.00184358, 0.00102426, 2.9683e-05, 6.01398e-05, 3.8493e-06, 4.34273e-07, 1.4649e-07]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot objective_classical on primary y-axis (normal scale)
ax1.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Objective')
ax1.tick_params(axis='y')
ax1.set_title('Case 3-AC-OPF-Classical_SPSolve: Iteration vs. Conditions')

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
