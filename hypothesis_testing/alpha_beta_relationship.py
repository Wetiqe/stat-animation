import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
sns.set_style('white')
plt.rc('font', size=18)

# Generate normal distributions with mean and standard deviation
mu0, mu1, sigma = 0, 3, 1
null_dist = norm(mu0, sigma)
alt_dist = norm(mu1, sigma)

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create a line plot for the null and alternative distributions
x = np.linspace(-4, 8, 1000)
y1 = 1-null_dist.cdf(x)
y2 = alt_dist.cdf(x)

# Plot the CDFs against each other
ax.plot(y1, y2)
# Plot a vertical line at x=0.05
ax.axvline(0.05, color='red', linestyle='--', label='α/significance level')
alpha = 0.05
index = np.where(y1 == 0.049918367838216016)
beta = round(alt_dist.cdf(x[index])[0], 2)
# annotate the coordinate of the intersection
ax.annotate(f'({alpha}, {beta})', (alpha, beta), fontsize=16)
# Add labels and a title
ax.set_xlim(-0.01, 1)
ax.set_ylim(-0.01, 1)
plt.legend(loc='upper right')
ax.set_xlabel('Type I Error Probability (α)')
ax.set_ylabel('Type II Error Probability (β)')
ax.set_title('Relationship Between α and β')
plt.savefig('alpha_beta_relationship.png', dpi=300)

fig2, ax = plt.subplots(figsize=(8, 6))
ax.plot(y1, 1-y2)
ax.set_xlabel('Type I Error Probability (α)')
ax.set_ylabel('Statistical testing power (1-β)')
ax.set_title('Relationship Between α and 1-β')
plt.savefig('alpha_power_relationship.png', dpi=300)