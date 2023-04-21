import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from scipy.stats import pearsonr, spearmanr
import seaborn as sns
sns.set_style('white')
# Generate x and y variables
np.random.seed(123)
x = np.random.normal(0, 1, 50)
y = np.random.binomial(1, 1 / (1 + np.exp(-(2 * x))), size=50)

# Fit logistic regression model
model = LogisticRegression()
model.fit(x.reshape(-1, 1), y)

# Plot the scatter plot with logistic regression line
x = np.linspace(-3, 3, 50)

y = model.predict_proba(x.reshape(-1, 1))[:, 1]
# Calculate correlation coefficients
pearson_corr, _ = pearsonr(x, y)
spearman_corr, _ = spearmanr(x, y)

# Plot the scatter plot with logistic regression line
fig, ax = plt.subplots(figsize=(8, 6))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='both', which='both', length=0)

plt.scatter(x, y)
plt.title(f"Pearson correlation = {pearson_corr:.2f}, Spearman correlation = {spearman_corr:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label="Linear regression")
plt.legend([])
plt.savefig('compare_corr_methods.png')
plt.show()
