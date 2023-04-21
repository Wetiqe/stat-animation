import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate some data
data = np.random.normal(size=1000)

# Define the number of bins for the histogram
num_bins = 20

# Create the figure and axis
fig, ax = plt.subplots()

# Define the x-axis limits
xlim = (min(data), max(data))

# Define the y-axis limits
ylim = (0, 150)

# Define the bar width
width = (xlim[1] - xlim[0]) / num_bins

# Define the bar colors
colors = plt.cm.viridis(np.linspace(0, 1, num_bins))

# Define the function to animate the histogram
def animate(frame):
    # Get the data up to the current frame
    data_slice = data[:frame*10]

    # Define the histogram
    hist, bins = np.histogram(data_slice, bins=num_bins, range=xlim)

    # Clear the previous histogram
    ax.clear()

    # Plot each bar of the histogram
    for i in range(num_bins):
        ax.bar(bins[i], hist[i], width=width, color=colors[i], alpha=0.5)

    # Set the x-axis and y-axis limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    # Set the title and labels
    ax.set_title('Histogram of Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=len(data), repeat=False)
animation.FuncAnimation(fig, animate, frames=100, repeat=True).save('histogram_drawing.gif', writer='Pillow')

# Show the animation
plt.show()

