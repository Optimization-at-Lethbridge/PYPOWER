import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 17)
objective_classical = [16355, 11416.928, 8610.6057, 8508.7646, 8475.4635, 8774.8169, 9883.6616, 9883.7187, 11965.514, 11965.619, 17480.252, 17479.979, 17479.907, 17479.898, 17479.897, 17479.897, 17479.897]
feascond_classical = [0.6, 0.522041, 0.453507, 0.433228, 414755, 0.378705, 0.225923, 0.225916, 0.126725, 0.12672, 2.18155e-13, 8.56156e-14, 2.36929e-16, 1.18468e-16, 3.55405e-16, 2.0732e-16, 3.25788e-16]
gradcond_classical = [2000, 1124.6, 348.933, 66.4603, 13.6677, 3.4666, 0.363525, 0.222051, 0.222034, 0.104076, 0.104066, 5.68383e-15, 1.40075e-14, 1.86766e-14, 1.42998e-14, 1.52363e-14, 7.9869e-15]
compcond_classical = [7.5, 4.41245, 2.70116, 2.39342, 1.92343, 1.49941, 0.745137, 1.05554, 0.449227, 0.406475, 0.673146, 0.0607822, 0.00608095, 0.000608117, 6.08119e-05, 6.0812e-06, 6.0812e-07]
costcond_classical = [0, 0.301912, 0.245782, 0.011826, 0.00391329, 0.0353158, 0.126352, 5.77795e-06, 0.210607, 8.78344e-06, 0.460835, 1.55967e-05, 4.13379e-06, 5.11174e-07, 5.07147e-08, 5.06802e-09, 5.06765e-10]

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
plt.title('Case 5-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')

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
