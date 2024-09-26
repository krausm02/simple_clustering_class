import numpy as np
import matplotlib.pyplot as plt


class clustering:
    """
    Create a clustering class for random data
    """
    def __init__(self, x, y, k, random_state=23):
        # If the user sent data
        if x.shape[0] > 0:
            self.x = x
            self.y = y
        else:
            raise Exception("x cannot be empty")
        # If the user sent a reasonable number of clusters
        if (k > 0) and (k <= x.shape[0]):
            self.k = k
        else:
            raise Exception("The number of clusters must be in the range (0, # points]")
        self.random_state = random_state


    def plot_blobs(self):
        """
        Plot the clusters and centers
        """
        fig = plt.figure(0)
        plt.grid(True)
        # if clusters exist, plot them
        if hasattr(self, 'clusters'):
            for i in self.clusters:
                center = self.clusters[i]['center']
                points = np.array(self.clusters[i]['points'])
                # If the current cluster contains points
                if points.shape[0] > 0:
                    plt.scatter(points[:,0], points[:,1])
                plt.scatter(center[0], center[1], marker='*', c='red')
            plt.show()
        else:
            raise Exception("Clusters must be initialized before plotting")


    def initialize_centroids(self):
        """
        Create random initial centroids for the clusters
        """
        self.clusters = {}
        np.random.seed(self.random_state)
        for idx in range(self.k):
            center = 2*(2*np.random.random((self.x.shape[1],))-1)
            cluster = {'center': center,
                    'points': [],
                    'dist': []}
            self.clusters[idx] = cluster


    def __distance(self, p1, p2):
        """
        Private distance function for cleanness (SSE error)
        """
        return np.sqrt(np.sum((p1-p2)**2))
    

    def assign_clusters(self):
        """
        Assigns each point to a cluster (E-step)
        """
        if hasattr(self, "clusters"):
            # for each point in our array
            for idx in range(self.x.shape[0]):
                dist = []
                curr_x = self.x[idx]

                # calculate the distance between the current point and each cluster
                for i in range(self.k):
                    dis = self.__distance(curr_x, self.clusters[i]['center'])
                    dist.append(dis)

                # assign the point to the closest cluster
                self.clusters[np.argmin(dist)]['points'].append(curr_x)
                # save the error for later
                self.clusters[np.argmin(dist)]['dist'].append(min(dist))
        else:
            raise Exception("Must initialize clusters before performing E-step")

    def update_centers(self):
        """
        Update the cluster centers by calculating the mean of all points in the cluster (M-step)
        """
        if hasattr(self, 'clusters'):
            for i in range(self.k):
                points = np.array(self.clusters[i]['points'])
                # if the cluster isn't empty, calculate the new center
                if points.shape[0] > 0:
                    new_center = points.mean(axis=0)
                    self.clusters[i]['center'] = new_center
        else:
            raise Exception("Must initialize clusters before performing M-step")

    def __calculate_error(self):
        """
        Private class to calculate the total SSE error across all clusters
        """
        error = 0
        for i in range(self.k):
            error += sum(self.clusters[i]['dist'])
        return error

    def reset_points(self):
        """
        Reset the points assigned to the current cluster if we are going to run E-step again
        """
        for i in range(self.k):
            points = np.array(self.clusters[i]['points'])
            # if the cluster isn't empty
            if points.shape[0] > 0:
                self.clusters[i]['points'] = []
                self.clusters[i]['dist'] = []

    def run_clustering(self, tol=1, print_flag=True):
        """
        Default clustering algorithm
        """
        self.initialize_centroids()
        error_old = 10000
        error = 3000
        i = 0

        while (error_old - error) > tol:

            # update error from the last iteration
            error_old = error
            self.reset_points()
            self.assign_clusters()
            self.update_centers()
            error = self.__calculate_error()

            # if we're on iteration 1, update error_old to ensure a second iteration
            if i == 0:
                error_old = error + tol + 1
            i += 1

            if print_flag:
                # print out the current progress
                print("Iteration {0:1d}, SSE: {1:.1f}".format(i, error))








