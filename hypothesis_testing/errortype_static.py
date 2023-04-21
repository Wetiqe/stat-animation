import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
sns.set_style('white')

# Generate normal distributions with mean and standard deviation
mu0, mu1, sigma = 0, 3, 1
null_dist = norm(mu0, sigma)
alt_dist = norm(mu1, sigma)

# Plot the null and alternative distributions
x = np.linspace(-4, 8, 1000)
plt.plot(x, null_dist.pdf(x), label='Null')
plt.plot(x, alt_dist.pdf(x), label='Alternative')

sample_mean = 2

# Shade the Type I error region
x_type1 = np.linspace(sample_mean, 4, 100)
plt.fill_between(x_type1, null_dist.pdf(x_type1), color='red', alpha=0.5, label='Type I Error')

# Shade the Type II error region
x_type2 = np.linspace(-4, sample_mean, 100)
plt.fill_between(x_type2, alt_dist.pdf(x_type2), color='blue', alpha=0.5, label='Type II Error')

# Add labels and legend
plt.title('Type I and Type II Errors')
plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.legend()
plt.savefig('type1_type2_errors.png', dpi=300)
# Display the plot
plt.show()
