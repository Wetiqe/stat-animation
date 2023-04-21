import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
plt.rcParams['font.family'] = 'Microsoft YaHei'

# 生成总体分布
mu = 0
sigma = 1
population = np.random.normal(mu, sigma, size=100000)

# 绘制总体分布直方图
plt.figure(figsize=(8, 6))

# 从总体中随机抽取样本
sample_size = 50
sample1 = np.random.choice(population, sample_size)
sample2 = np.random.choice(population, sample_size)
sample3 = np.random.choice(population, sample_size)

# 绘制样本分布直方图
plt.hist(sample1, bins=10, alpha=0.5, density=True, label='Sample 1')
plt.hist(sample2, bins=10, alpha=0.5, density=True, label='Sample 2')
plt.hist(sample3, bins=10, alpha=0.5, density=True, label='Sample 3')

# 绘制抽样分布直方图
mean_samples = [sample1.mean(), sample2.mean(), sample3.mean()]
plt.hist(mean_samples, bins=3, alpha=1, rwidth = 0.8,density=True, color='red',label='Sampling Distribution')

# 添加图例和标签
plt.legend(loc='best')
plt.xlabel('Z 值')
plt.ylabel('概率密度')
plt.ylim(0,0.6)
plt.title('总体分布，样本分布，抽样分布')
# plt.savefig('samp_distribution.png')

# 显示图形
plt.show()
