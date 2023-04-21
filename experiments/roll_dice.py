import random
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['SimHei']
# Define the probabilities of rolling each number on the unbalanced dice
probabilities = [0.12, 0.15, 0.15, 0.15, 0.15, 0.28]

def roll(num_rolls):
    # Count the number of times each number is rolled
    observed_counts = [0, 0, 0, 0, 0, 0]
    for i in range(num_rolls):
        roll = random.choices(range(1, 7), weights=probabilities)[0]
        observed_counts[roll - 1] += 1
    observed_probabilities = [c / num_rolls for c in observed_counts]

    return observed_counts, observed_probabilities,

def plot_prob(observed_counts, observed_probabilities):
    num_rolls = np.array(observed_counts).sum()
    numbers = np.arange(1, 7)
    plt.bar(numbers, observed_counts)
    plt.title(f"投掷筛子{num_rolls}次")
    plt.xlabel("点数")
    plt.ylabel("频数")
    plt.show()
    if num_rolls <101:
        return None
    plt.bar(numbers, observed_probabilities,label='后验概率')
    plt.bar(numbers, probabilities, alpha=0.7,label='先验概率')
    plt.legend()
    plt.title("检测骰子是否有问题")
    plt.xlabel("点数")
    plt.ylabel("后验概率")
    plt.show()

# Print the observed counts and theoretical probabilities for each number
# for i in range(6):
#     print(f"Number {i+1}: Observed count = {observed_counts[i]}, Observed probability = {observed_probabilities[i]}, Theoretical probability = {theoretical_probabilities[i]}")


if __name__ == '__main__':
    while True:
        num_rolls = int(input("请输入投掷次数："))
        if num_rolls == 0:
            break
        observed_counts, observed_probabilities = roll(num_rolls)
        plot_prob(observed_counts, observed_probabilities)
