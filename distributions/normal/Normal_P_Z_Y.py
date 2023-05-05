import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import scipy.stats

sns.set_style('white')
font_size = 40
plt.rcParams.update({'font.size': font_size})

fig, ax = plt.subplots(figsize=(32, 18))
ax.set_xlim(-4, 4)
ax.tick_params(axis='x', labelsize=10)
ax.set_ylim(0, 0.5)
ax.set_xlabel('Z value')
ax.set_ylabel('Y Value (Probability density)')
ax.set_title('P value and Z value in normal distribution')
#plot normal distribution curve
x = np.linspace(-4, 4, 100)
y = scipy.stats.norm.pdf(x)
ax.plot(x, y, color='blue')
ax.axvline(x=1.65, color='#8B0000', linestyle='--', linewidth=2, label='One-sided 5%')
ax.axvline(x=1.96, color='#006400', linestyle='--', linewidth=2, label='Two-sided 5%')

#initialize fill and text objects
text = ax.text(-3.5, 0.45, 'P value = ')
#define animation function
def animate(i):
    #calculate z value and p value

    z = i/100
    p = 0.5 - scipy.stats.norm.sf(abs(z))
    ax.set_xticks([-4, -3, -2,  -1,  0, z, 1.65,1.96, 4], )
    ax.tick_params(axis='x', labelsize=font_size)
    if i == 0:
        global z_line
        z_line = ax.axvline(x=z, color='black', linestyle='-', linewidth=2, label='Current Z value ')
    if i != 0:
        z_line.remove()
        z_line = ax.axvline(x=z, color='black', linestyle='-', linewidth=2, label='Current Z value ')

    #update fill and text objects
    z_range = np.linspace(0,z,100)
    y_range = scipy.stats.norm.pdf(z_range)
    fill = ax.fill_between(z_range, y_range, color='red')
    # Display the P value and Z value at right side
    text.set_text('P value = ' + str(round(p, 3)) + '\nZ value = ' + str(round(z, 2)))
    text.set_position((2.1, 0.3))

    return fill, text

#run animation
plt.legend(loc='upper right', )
plt.tight_layout()
ani = animation.FuncAnimation(fig, animate, frames=400, interval=200, blit=True)
ani.save('Normal_P_Z_Y.gif', writer='imagemagick', fps=20)
plt.show()
