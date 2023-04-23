import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

sns.set_style('white')
# Set the confidence level and degrees of freedom
alpha = 0.05
font_size = 16
# Calculate the critical value for the normal distribution
name = 'normal'
if name == 'normal':
    distribution = stats.norm
elif name == 't':
    df = 20 # degree of freedom
    distribution = stats.t
else:
    raise ValueError('Distribution name must be normal or t')

crit_val = distribution.ppf(1-alpha/2)
crit_val_y = distribution.pdf(crit_val)
# Generate x-axis values for the normal distribution plot
x = np.linspace(-4, 4, 500)

# Generate y-axis values for the normal distribution plot
y = distribution.pdf(x, 0, 1)

# Create the plot and label the axes
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, color='black', label='normal distribution')
ax.set_xlabel('z value',fontsize=font_size)
ax.set_ylabel('Probability density',fontsize=font_size)
ax.set_title('Significance Level and Acceptance/Rejection Areas Under Normal Distribution',fontsize=font_size)

# Shade the acceptance and rejection areas
alpha = 0.05
transparent = 0.6
ax.axvline(x=-crit_val, color='red', linestyle='--', label='α/significance level')
ax.axvline(x=crit_val, color='red', linestyle='--')
ax.fill_betweenx(y, x, -crit_val, where=(x < -crit_val), alpha=transparent, color='green', label='acceptance area')
ax.fill_betweenx(y, x, crit_val, where=(x > crit_val), alpha=transparent, color='green')
ax.fill_between(np.array([-crit_val,crit_val]),y1=crit_val_y, alpha=transparent, color='red', label='rejection area')
ax.fill_betweenx(y, x, crit_val, where=(x > -crit_val)&(x < crit_val), alpha=transparent, color='red', )

# Add legend
ax.legend(fontsize=14)
plt.savefig(f'hypothesis_testing_{name}.png', dpi=300)
plt.show()