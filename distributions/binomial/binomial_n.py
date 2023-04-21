import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def binomial_dist(n, p):
    # Generate the x values (number of successes)
    x = np.arange(0, n+1)

    # Compute the corresponding binomial probabilities
    binom_probs = np.zeros(n+1)
    for k in range(n+1):
        binom_probs[k] = np.math.comb(n, k) * p**k * (1-p)**(n-k)

    return x, binom_probs

def plot_binomial_dist(x, binom_probs, p):
    plt.bar(x, binom_probs)
    plt.title(f"Binomial Distribution (n={len(x)-1}, p={p:.2f})")
    plt.xlabel("number of successes")
    plt.ylabel("probability")

def update(frame):
    ax.clear()
    ax.set_ylim(0,1)
    global p
    p = frame*2/100
    x, binom_probs = binomial_dist(n, p)
    plot_binomial_dist(x, binom_probs, p)

if __name__ == '__main__':
    ns = list(map(int, input("Enter the values of n separated by spaces: ").split()))
    for n in ns:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_ylim(0,1)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.tick_params(axis='both', which='both', length=0)
        ani = FuncAnimation(fig, update, frames=np.arange(0, 51), interval=100, repeat=False)
        ani.save(f'binomial{n}.gif', writer='pillow')
        plt.show()