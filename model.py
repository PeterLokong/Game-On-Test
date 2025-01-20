# 🌍✨ "Unlocking the Rhythms of Data: A Journey Through the Heartbeat of PCA in the African Plains" ✨🌍
# I'm Kidding guys, this is yours faithfully - Mr. Lokong
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.decomposition import PCA

#Here we are going to initialize the Random Number Generator and Set the necessary Parameters
rng = np.random.RandomState(0)
n_samples = 500
cov_matrix = [[3, 3], [3, 4]]

#Next:  We Generate Synthetic data using Multivariate Normal Distribution
X = rng.multivariate_normal(mean=[0, 0], cov=cov_matrix, size=n_samples)

#Let us apply the PCA to the data , reducing to 2 components
pca_model = PCA(n_components=2).fit(X)

#Let us the create the scatter plot for the data
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="Samples")

#Plot the Principal Componetnts, Scaled by their explained variance
for idx, (component, variance) in enumerate(zip(pca_model.components_, pca_model.explained_variance_)):
    scaled_component = component * variance
    plt.plot(
        [0, scaled_component[0]],
        [0, scaled_component[1]],
        label=f"Principal Component {idx}",
        linewidth=5,
        color=f"C{idx + 2}",
    )

#We then set the plot aesthetics
plt.gca().set(
    aspect="equal",
    title="2D Datasheet with Principal Components by lokong",
    xlabel="First Feature",
    ylabel="Second Feature",
)

#Finally!!!!: Let us now display the legend and the save the plot
plt.legend()
plt.savefig("pca_plot.png", dpi=300)