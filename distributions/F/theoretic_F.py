# Plot theoretical distribution animation
import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

plt.rcParams.update({'font.size': 18})
sns.set_style('white')


class F_anim(object):

    def __init__(self, dfn=None, dfd=None,plot_sig=False,alpha=0.05, ylim=((0,1)),xlim=((-0.5,3))):
        self.x_values = np.linspace(0, 4, 1000)
        self.dfn = dfn if dfn else None
        self.dfd = dfd if dfd else None
        self.plot_sig = plot_sig
        self.alpha = alpha
        self.ylim = ylim if dfn or dfd else ((0,4))
        self.xlim = xlim

    def distribution(self, frame):
        if self.plot_sig:
            ax.clear()
        ax.set_ylim(self.ylim)
        ax.set_xlim(self.xlim)
        x = self.x_values
        dof = frame + 1
        dfn = self.dfn if self.dfn else dof
        dfd = self.dfd if self.dfd else dof
        ax.set_title('F-Distribution \n'
                     'Numerator dof = {}, Denominator dof = {}'.format(dfn, dfd), fontsize=18)
        y_values = f.pdf(x, dfn=dfn, dfd=dfd)
        color = plt.cm.coolwarm((frame) / 50)  # generate color based on frame number
        fplot = ax.plot(x, y_values, lw=2, color=color, alpha=1)
        if self.plot_sig:
            # Plot the rejection area
            transparent = 0.6
            crit_val = f.ppf(1-self.alpha/2, dfn=dfn, dfd=dfd)
            crit_val_y = f.pdf(crit_val, dfn=dfn, dfd=dfd)
            small_crit_val = f.ppf(self.alpha/2, dfn=dfn, dfd=dfd)
            neg_crit_val_y = f.pdf(small_crit_val, dfn=dfn, dfd=dfd)
            y = f.pdf(x, dfn=dfn, dfd=dfd)
            ax.axvline(x=crit_val, color='red', linestyle='--', label='α/significance level')
            ax.axvline(x=small_crit_val, color='red', linestyle='--')
            ax.fill_betweenx(y, x, small_crit_val, where=(x < small_crit_val), alpha=transparent, color='red', label='rejection area')
            ax.fill_betweenx(y, x, crit_val, where=(x > crit_val), alpha=transparent, color='red')
            plt.legend(loc='upper right')
        return fplot,


setting = {
    'animate': {
        'frames': 100,
        'interval': 100,
        'repeat': False,
    },
    'save': {
        'writer': 'pillow',
        'fps': 5,
    },
}
# Generate the x-axis values
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel('F')
ax.set_ylabel('Probability Density')
FuncAnimation(fig, F_anim(dfn=10).distribution, **setting['animate']).save('F_dfd_change.gif', **setting['save'])
ax.clear()
FuncAnimation(fig, F_anim(dfd=10).distribution, **setting['animate']).save('F_dfn_change.gif', **setting['save'])
ax.clear()
ax.set_ylim(0, 4)
FuncAnimation(fig, F_anim().distribution, **setting['animate']).save('F_both_change.gif', **setting['save'])
ax.clear()
FuncAnimation(fig, F_anim(dfn=10,dfd=None,plot_sig=True).distribution, **setting['animate']).save('F_sig.gif', **setting['save'])
