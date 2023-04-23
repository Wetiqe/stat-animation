import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
from matplotlib.animation import FuncAnimation

sns.set_style('white')

# Generate normal distributions with mean and standard deviation
mu0, mu1 = 0, 4

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-4, 8, 1000)

# Set the x and y limits for the plot
ax.set_xlim([-4, 8])
ax.set_ylim([0, 0.5])

# Define a function to update the shaded regions with the sigma value
def update(frame):
    ax.clear()
    sample_mean = 2
    sigma = (130-frame)/50
    # Create a line plot for the null and alternative distributions
    null_dist = norm(mu0, sigma)
    alt_dist = norm(mu1, sigma)
    plt.plot(x, null_dist.pdf(x), label='Null')
    plt.plot(x, alt_dist.pdf(x), label='Alternative')

    # Shade the Type I error region
    x_type1 = np.linspace(sample_mean, 8, 100)
    plt.fill_between(x_type1, null_dist.pdf(x_type1), color='red', alpha=0.5, label='Type I Error')

    # Shade the Type II error region
    x_type2 = np.linspace(-4, sample_mean, 100)
    plt.fill_between(x_type2, alt_dist.pdf(x_type2), color='blue', alpha=0.5, label='Type II Error')
    ax.set_xlabel('Sample Mean',fontsize=16)
    ax.set_ylabel('Probability Density',fontsize=16)
    ax.legend(fontsize=14, loc='upper right')
    # Update the title with the current sample mean
    ax.set_title(f'Type I and Type II Errors (Standard Error = {sigma:.2f})', fontsize=18)

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=150)

# Save the animation as a GIF file
ani.save('error_reduction.gif', writer='pillow', dpi=300)

# Display the plot
plt.show()
