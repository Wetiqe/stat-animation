import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
from matplotlib.animation import FuncAnimation

sns.set_style('white')

# Generate normal distributions with mean and standard deviation
mu0, mu1, sigma = 0, 3, 1
null_dist = norm(mu0, sigma)
alt_dist = norm(mu1, sigma)

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create a line plot for the null and alternative distributions
x = np.linspace(-4, 8, 1000)
null_line, = ax.plot(x, null_dist.pdf(x), label='Null')
alt_line, = ax.plot(x, alt_dist.pdf(x), label='Alternative')

# Set the x and y limits for the plot
ax.set_xlim([-4, 8])
ax.set_ylim([0, 0.5])

# Define a function to update the shaded regions with the sample mean
def update(frame):
    ax.clear()
    # Create a line plot for the null and alternative distributions
    plt.plot(x, null_dist.pdf(x), label='Null')
    plt.plot(x, alt_dist.pdf(x), label='Alternative')

    sample_mean = frame*3/50

    # Shade the Type I error region
    x_type1 = np.linspace(sample_mean, 4, 100)
    plt.fill_between(x_type1, null_dist.pdf(x_type1), color='red', alpha=0.5, label='Type I Error')

    # Shade the Type II error region
    x_type2 = np.linspace(-4, sample_mean, 100)
    plt.fill_between(x_type2, alt_dist.pdf(x_type2), color='blue', alpha=0.5, label='Type II Error')
    ax.set_xlabel('Sample Mean',fontsize=16)
    ax.set_ylabel('Probability Density',fontsize=16)
    ax.legend(fontsize=14)
    # Update the title with the current sample mean
    ax.set_title(f'Type I and Type II Errors (Sample Mean = {sample_mean:.2f})', fontsize=18)

# Create the animation
ani = FuncAnimation(fig, update, frames=50, interval=100)

# Save the animation as a GIF file
ani.save('type1_type2_errors.gif', writer='pillow', dpi=300)

# Display the plot
plt.show()
