import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define data for plotting
iterations_classical = range(0, 9)
objective_classical = [7278.125,4131.0268,4131.0266,4131.0266,4131.0266,4131.0266,4131.0266,4131.0266,4131.0266]
feascond_classical = [0.3875,1.54021e-12,9.18691e-14,4.4943e-17,4.4943e-17,4.4943e-17,4.4943e-17,4.4943e-17,4.4943e-17]
gradcond_classical = [1765,0.13735,6.05359e-15,5.67158e-15,3.50816e-15,7.63431e-15,3.6859e-15,5.0077e-15,3.19368e-15]
compcond_classical = [19.5686,9.7069,0.970668,0.0970665,0.00970665,0.000970665,9.70665e-05,9.70665e-06,9.70665e-07]
costcond_classical = [0,0.432346,3.99544e-08,2.64865e-10,2.58474e-12,2.57527e-14,2.20109e-16,0,2.20109e-16]

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
plt.title('Case 9-DC-OPF-Classical_SPSolve: Iteration vs. Conditions')
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