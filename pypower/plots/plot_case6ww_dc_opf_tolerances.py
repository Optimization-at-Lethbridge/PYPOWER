import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 10)
objective_classical = [3901.2551,2584.3501,2394.4442,2393.4827,2393.3198,2393.3128,2393.3125,2393.3125,2393.3125,2393.3125]
feascond_classical = [0.555556,0.0642891,1.4045e-14,5.3408e-16,1.3324e-16,8.88181e-17,4.44089e-17,4.44089e-17,4.44089e-17,4.44089e-17]
gradcond_classical = [650.075,0.105407,0.000421522,2.51256e-15,3.48091e-15,6.04277e-15,4.02243e-15,2.85459e-15,1.91308e-15,6.20741e-15]
compcond_classical = [12.4444,10.7121,2.77182,0.342202,0.0369565,0.00370081,0.000370086,3.70087e-05,3.70087e-06,3.70087e-07]
costcond_classical = [0,0.337473,0.0734546,0.000401405,6.80397e-05,2.92638e-06,9.76409e-08,9.34946e-09,9.344455e-10,9.34412e-11]

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
plt.title('Case 6ww-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')
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