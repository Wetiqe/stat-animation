import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
# 设定随机种子，以保证每次运行生成的数据相同
np.random.seed(42)

# 生成一个均值为0，标准差为1的正态分布随机数（样本容量为10000）
data = np.random.normal(0, 1, size=10000)

# 计算数据的平均值和标准差
mean = np.mean(data)
std = np.std(data)

# 计算均值加减两倍标准差的边界值
lower_bound = mean - 2*std
upper_bound = mean + 2*std

# 绘制数据的直方图
plt.hist(data, bins=50, density=True, alpha=0.5, color='blue')

# 绘制平均值和标准差的参考线
plt.axvline(mean, color='red', linestyle='--', linewidth=1)
plt.axvline(lower_bound, color='green', linestyle='--', linewidth=1)
plt.axvline(upper_bound, color='green', linestyle='--', linewidth=1)

# 添加图例和标题
plt.legend(['Mean', '95% data interval'])
plt.title('Normal Distribution with 95% data interval')
plt.savefig('normal_95.png', dpi=300)
# 显示图形
plt.show()