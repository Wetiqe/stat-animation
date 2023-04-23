import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
plt.rc('font', size=18)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# Plot for two-sided hypothesis testing
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)
ax1.plot(x, y, 'k-', linewidth=2)
ax1.axvline(x=-1.96, color='b', linestyle='--', linewidth=2)
ax1.axvline(x=1.96, color='b', linestyle='--', linewidth=2)
ax1.fill_between(x, y, where=(x <= -1.96) | (x >= 1.96), color='gray', alpha=0.3)
ax1.set_title('Two-sided Hypothesis Testing')
ax1.set_xlabel('Test Statistic')
ax1.set_ylabel('Probability Density')

# Plot for one-sided hypothesis testing
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)
ax2.plot(x, y, 'k-', linewidth=2)
ax2.axvline(x=1.645, color='r', linestyle='--', linewidth=2)
ax2.fill_between(x, y, where=x >= 1.645, color='gray', alpha=0.3)
ax2.set_title('One-sided Hypothesis Testing')
ax2.set_xlabel('Test Statistic')
ax2.set_ylabel('Probability Density')
plt.tight_layout()
plt.savefig('one_side_testing.png', dpi=300)
# Show the plot
plt.show()
