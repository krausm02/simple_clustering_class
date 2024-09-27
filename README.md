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

Set up a virtual environment (optional):  

    pip install virtualenv
    python -m venv myenv
    source myenv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Example warmstart file:

    run_clustering.py

## Methods
1. **clustering(x, k, random_state)**  
        Creates the class instance  
    **Parameters**  
        **x** : ndarray of shape (n_samples, n_features)  
            The generated samples  
        **k** : int  
            The number of clusters  
        **random_state** : int (optional)  
            Random integer for initializing centers  

2. **run_clustering()**  
        Performs the clustering operation, matches points to centers  
3. **plot_clusters()**  
        Creates a colocoded plot showing the point clusters and centers
