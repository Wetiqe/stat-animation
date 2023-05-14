# Plot theoretical distribution animation
import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
plt.rcParams.update({'font.size': 18})
sns.set_style('white')

# Generate the x-axis values
x_values = np.linspace(0, 35, 1000)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel('chi 2', fontsize=16)
ax.set_ylabel('Density', fontsize=16)

# Define the animation function
def animate(frame):
    dof = frame+1
    ax.set_ylim(0,0.25)
    ax.set_xlim(-0.5, 35)
    color = plt.cm.coolwarm((frame)/30)  # generate color based on frame number
    y_values = chi2.pdf(x_values, df=dof)
    chi2plot = ax.plot(x_values, y_values, 'r-', lw=2,color=color, alpha=1 )
    ax.set_title('chi2-Distribution with dof = {}'.format(dof), fontsize=18)
    return chi2plot,

# Create the animation
anim = FuncAnimation(fig, animate, frames=30, interval=100, repeat=False)

# Save the animation as a gif
anim.save('theo_chi2.gif', writer='pillow', fps=5)

# Show the plot
plt.show()
