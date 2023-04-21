import random
import matplotlib.pyplot as plt
import numpy as np
import math

# Calculate the mean and standard deviation of the sample
def plot_hist(data):
    sample_mean = np.mean(data)
    sample_std = np.std(data)

    # Print the sample mean and standard deviation
    print(f"Sample mean reaction time (ms): {sample_mean:.2f}")
    print(f"Sample standard deviation : {sample_std:.2f}")
    num_trials = len(data)
    if num_trials <100:
        num_bins = 10
    else:
        num_bins = int(math.sqrt(num_trials))
    # Create a histogram of the sample heights
    plt.hist(data, bins=num_bins, density=True)
    plt.xlabel("reaction time (ms)")
    plt.ylabel("frequency")
    plt.show()


# Define the mean and standard deviation of the normal distribution
mu = 500
sigma = 50

if __name__ == '__main__':
    while True:
        num_trial = int(input("Enter the number of trials: "))
        if num_trial == 0:
            break
        reaction = [random.normalvariate(mu, sigma) for i in range(num_trial)]
        plot_hist(reaction)