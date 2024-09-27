# Clustering Class for 2-Feature Data

A generic clustering class for 2-feature data provided by the user. This class is based on a simple overview provided by [K means Clustering - Introduction] (https://www.geeksforgeeks.org/k-means-clustering-introduction/)

## Prerequisites:

Required:

    numpy
    matplotlib
    python 3.11

Recommended:

    sklearn
    virtualenv

## Running Locally:

1. Set up a virtual environment (optional):

    pip install virtualenv
    python -m venv myenv
    source myenv/bin/activate

2. Install dependencies:

    pip install -r requirements.txt

3. Enter parameters in run_clustering
  - k = 6               # Number of clusters
  - random_state = 23   # Random state for initialization
  - n_samples = 1000    # Number of samples in all groups
  - n_features = 2      # Number of features in vector for each sample
  - centers = 6         # Number of groups of initial samples