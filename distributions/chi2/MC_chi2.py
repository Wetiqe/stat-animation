# Monto Carlo Method
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# 生成一个随机分布
plt.rcParams.update({'font.size': 18})
sns.set_style('white')

np.random.seed(123)
# generate x from standard normal distribution
x = np.random.randn(10000)

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 6))
fontsize = 16

# Initialize histogram and line
bins = np.linspace(0, 4, 51)
hists = []
lines = []

for i in range(51):
    hist, = ax.plot([], [], lw=2, alpha=0.5)
    hists.append(hist)
    line, = ax.plot([], [], 'r', lw=2)
    lines.append(line)

# Update drawing function
def update(frame):
    ax.clear() # clear the axes before drawing each new frame
    ax.set_xlim(-1, 35)
    ax.set_ylim(0, 0.25)
    ax.set_xlabel('Chi square',fontsize=fontsize)
    ax.set_ylabel('Density',fontsize=fontsize)
    sample_size = frame + 1
    stds = []
    for i in range(1, 3000):
        sample = np.random.choice(x, sample_size)
        stds.append((np.array(sample)**2).sum())
    stds = np.array(stds)

    # Update histogram and line
    hist, line = hists[frame], lines[frame]
    sns.kdeplot(stds,ax=ax,shade=True,color='b')
    ax.set_title(f"Demonstration of Chi Square Distribution with dof (n={sample_size})", fontsize=fontsize)

    return hist, line


# Create animation
anim = FuncAnimation(fig, update, frames=30, interval=100, blit=True)
anim.save('MC_chi2.gif', writer='Pillow', fps=5)
# Show animation
plt.show()
