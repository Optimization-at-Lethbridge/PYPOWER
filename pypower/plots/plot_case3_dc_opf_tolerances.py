import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 9)
objective_classical = [750,746.25084,746.25002,746.25,746.25,746.25,746.25,746.25,746.25]
feascond_classical = [0.55, 1.93783e-14,8.12379e-17,4.0618e-17,0,4.0617e-17,8.12358e-17,8.12358e-17,8.12358e-17]
gradcond_classical = [300, 8.848e-16,4.95311e-15,1.00234e-15,1.88841e-15,1.16409e-15,2.5259e-15,5.9412e-15,3.31269e-15]
compcond_classical = [5, 3.97906,0.398261,0.0398347,0.00398355,0.000398356,3.983e-05,3.98356e-06,3.98356e-07]
costcond_classical = [0, 0.00499222,1.10896e-06,2.06489e-08,1.90559e-10,1.88274e-12,1.88654e-14,3.04281e-16,0]

# Define colorblind-friendly palette
colors = cm.get_cmap('tab10').colors

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot each condition with appropriate styles and labels
plt.plot(iterations_classical, objective_classical, marker='o', linestyle='-', color=colors[0], label='Objective')
plt.plot(iterations_classical, feascond_classical, marker='s', linestyle='solid', color=colors[1], label='Feascond')
plt.plot(iterations_classical, gradcond_classical, marker='^', linestyle='dashed', color=colors[2], label='Gradcond')
plt.plot(iterations_classical, compcond_classical, marker='D', linestyle='dashdot', color=colors[3], label='Compcond')
plt.plot(iterations_classical, costcond_classical, marker='x', linestyle='dotted', color=colors[4], label='Costcond')

# Add labels and title
plt.xlabel('Iteration')
plt.ylabel('Conditions')
plt.title('Case 3-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')
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
