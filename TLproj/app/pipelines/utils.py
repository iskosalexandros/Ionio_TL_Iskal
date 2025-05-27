import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import seaborn as sns


def plot_pca():
    # Παράδειγμα με τυχαία δεδομένα
    data = np.random.rand(100, 10)
    coords = PCA(n_components=2).fit_transform(data)
    fig, ax = plt.subplots()
    ax.scatter(coords[:, 0], coords[:, 1])
    ax.set_title('PCA')
    return fig


def plot_heatmap():
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots()
    sns.heatmap(data, ax=ax)
    ax.set_title('Heatmap')
    return fig
