import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t
import seaborn as sns
from matplotlib.animation import FuncAnimation

sns.set_style('white')
# Set parameters for the normal distribution
mu = 0
sigma = 1

# Generate the x-axis values
x = np.linspace(-4, 4, 1000)

# Calculate the probability density function (PDF) values for the normal distribution
normal_pdf = norm.pdf(x, mu, sigma)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('Density', fontsize=16)
normal_plot, = ax.plot(x, normal_pdf, label='Normal Distribution', color='blue', alpha=0.7, linewidth=3)

# Define the animation function
def animate(frame):
    dof = frame+1
    t_pdf = t.pdf(x, dof)
    color = plt.cm.Reds((frame+30)/100)  # generate color based on frame number
    t_plot, = ax.plot(x, t_pdf,color=color, alpha=0.7, linewidth=2)
    ax.set_title('t-Distribution with dof = {}'.format(dof), fontsize=18)
    ax.legend(fontsize=12)
    return t_plot,

# Create the animation
anim = FuncAnimation(fig, animate, frames=50, interval=100, repeat=False)

# Save the animation as a gif
anim.save('t_distributions.gif', writer='pillow', fps=5)

# Show the plot
plt.show()
