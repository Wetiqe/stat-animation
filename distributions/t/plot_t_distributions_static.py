import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t
import seaborn as sns
sns.set_style('white')
# Set parameters for the normal distribution
mu = 0
sigma = 1

# Set parameters for the t-distribution
dof_values = [2,5, 10, 30]  # degrees of freedom

# Generate the x-axis values
x = np.linspace(-5, 5, 1000)

# Calculate the probability density function (PDF) values for the normal distribution
normal_pdf = norm.pdf(x, mu, sigma)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, normal_pdf, label='Normal Distribution', color='blue', alpha=0.7, linewidth=3)

# Calculate the PDF values for the t-distribution with different dof values and plot them
for dof, color in zip(dof_values, ['red',  'orange','yellow', 'green',]):
    t_pdf = t.pdf(x, dof)
    plt.plot(x, t_pdf, label=f't-Distribution (dof={dof})', color=color, alpha=0.7, linewidth=2)

plt.xlabel('x', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.legend(fontsize=12)
plt.title('Comparison of Normal Distribution and t-Distribution', fontsize=16)
plt.savefig('t_distributions.png', dpi=300)
# Show the plot
plt.show()
