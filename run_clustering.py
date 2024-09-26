from clustering import clustering
from sklearn.datasets import make_blobs

k = 6               # Number of clusters
random_state = 23   # Random state for initialization
n_samples = 1000    # Number of samples in all groups
n_features = 2      # Number of features in vector for each sample
centers = 6         # Number of groups of initial samples
x,y = make_blobs(n_samples=n_samples,
                 n_features=n_features, 
                 centers=centers, 
                 random_state=random_state)
s = clustering(x, y, k, random_state)
s.run_clustering()
s.plot_blobs()