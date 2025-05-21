import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

# Create a synthetic "S-curve" dataset
X, color = datasets.make_s_curve(n_samples=1000, noise=0.05, random_state=0)

# Apply Isomap
isomap = manifold.Isomap(n_neighbors=10, n_components=2)
X_isomap = isomap.fit_transform(X)

# Apply Locally Linear Embedding (LLE)
lle = manifold.LocallyLinearEmbedding(n_neighbors=10, n_components=2, method='standard')
X_lle = lle.fit_transform(X)

# Plotting original data and the results
fig = plt.figure(figsize=(18, 5))

# Original 3D data
ax = fig.add_subplot(131, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.set_title("Original 3D S-Curve")

# Isomap result
ax = fig.add_subplot(132)
ax.scatter(X_isomap[:, 0], X_isomap[:, 1], c=color, cmap=plt.cm.Spectral)
ax.set_title("Isomap Embedding (2D)")

# LLE result
ax = fig.add_subplot(133)
ax.scatter(X_lle[:, 0], X_lle[:, 1], c=color, cmap=plt.cm.Spectral)
ax.set_title("LLE Embedding (2D)")

plt.tight_layout()
plt.show()
