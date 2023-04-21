import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
# 生成一个随机分布
sns.set_style('white')

np.random.seed(123)
x = np.random.exponential(1, size=1000)
sns.displot(x, kde=True)
plt.savefig('exp.png')
sample_size = 100
means = []
for i in range(1, 1000):
    sample = np.random.choice(x, sample_size)
    means.append(np.mean(sample))
means = np.array(means)
# 计算均值和标准差
mu = np.mean(means)
sigma = np.std(means)

# 绘制样本均值分布
plt.figure(figsize=(8, 6))
plt.hist(means, bins=50, density=True, alpha=0.5, label='Sample Means')
# 绘制正态分布曲线
x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
y_norm = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x_norm - mu) / sigma)**2)
plt.plot(x_norm, y_norm, 'r', linewidth=2, label='Normal')

# 添加图例和标签
plt.legend(loc='best')
plt.xlabel('Sample Means')
plt.ylabel('Density')
plt.title('Sampling Distribution of the Mean')
plt.savefig('sampling_distribution_of_the_mean.png')
# 显示图形
plt.show()


fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
fontsize = 16
ax.set_xlabel('Sample Mean',fontsize=fontsize)
ax.set_ylabel('Density',fontsize=fontsize)
ax.axvline(x=1, linestyle='--', color='red')
# 初始化直方图和曲线
bins = np.linspace(0, 4, 51)
hists = []
lines = []


for i in range(51):
    hist, = ax.plot([], [], lw=2, alpha=0.5)
    hists.append(hist)
    line, = ax.plot([], [], 'r', lw=2)
    lines.append(line)

# 更新绘图函数
def update(frame):
    sample_size = frame + 1
    means = []
    for i in range(1, 1000):
        sample = np.random.choice(x, sample_size)
        means.append(np.mean(sample))
    means = np.array(means)

    # 更新直方图和曲线
    hist, line = hists[frame], lines[frame]
    hist.set_data(np.histogram(means, bins=bins[1:])[1], np.histogram(means, bins=bins, density=True)[0])
    ax.set_title(f"Demonstration of Central Limit Theorem and Law of Large Numbers (n={sample_size})", fontsize=fontsize)

    return hist, line

# 创建动画
anim = FuncAnimation(fig, update, frames=50, interval=100, blit=True)
anim.save('sample_mean.gif', writer='Pillow', fps=10)
# 显示动画
plt.show()
