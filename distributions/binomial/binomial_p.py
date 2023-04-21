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

def update(frame):
    ax.clear()
    n = frame + 1
    x, binom_probs = binomial_dist(n, p)

    ax.bar(x, binom_probs)
    ax.set_title(f"Binomial (n={n}, p={p:.2f})")


if __name__ == '__main__':
    ps = list(map(float, input("Enter the values of p separated by spaces: ").split()))
    for p in ps:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xlabel("number of successes")
        ax.set_ylabel("probability")
        ax.tick_params(axis='both', which='both', length=0)
        ani = FuncAnimation(fig, update, frames=60, repeat=False)
        ani.save(f'binomial_p{p}.gif', writer='pillow')
        plt.show()

