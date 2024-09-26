import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize

print("...........Clustering..............")
dataset = pd.read_csv("C:/Users/Roopashree obalesh/Desktop/diabetes.csv") 
print(dataset.head())

i=0

while i <= 3:
    print("Select operation.")
    print("1.Hierchical clustering ")
    print("2.k-means")
    print("3.Fuzzy k-means")
    print("4.Exit")

    choice = input("Enter Your choice(1/2/3/4):")

    if choice == '1':
        print("Hierchical clustering")
        x=dataset.iloc[:,[0,1]].values
        dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
        plt.show()
    
    elif choice == '2':
    
        datascale=normalize(dataset)
        datascale=pd.DataFrame(datascale,columns=dataset.columns)
        print(datascale.head())
        km=KMeans(n_clusters=2)
        km.fit(datascale)
        plt.figure(figsize=(10,7))
        plt.scatter(datascale['Age'],datascale['BMI'],c=km.labels_) 
        plt.show()
  
    elif choice == '3':

        print("Fuzzy k-means")
        np.random.seed(0)
        batch_size = 45
        centers = [[1, 1], [-1, -1], [1, -1]]
        n_clusters = len(centers)
        X, labels_true = make_blobs(n_samples=1200, centers=centers, cluster_std=0.3)
        kmeans = KMeans(k=3)
        kmeans.fit(X)

        kmedians = KMedians(k=3)
        kmedians.fit(X)

 
        fuzzy_kmeans = FuzzyKMeans(k=3, m=2)
        fuzzy_kmeans.fit(X)

        print('KMEANS')
        print(kmeans.cluster_centers_)

        print('KMEDIANS')
        print(kmedians.cluster_centers_)

        print('FUZZY_KMEANS')
        print(fuzzy_kmeans.cluster_centers_)

          
    elif choice=='4':
        print("Exiting.................")
        break
        
    else:
       print("Invalid input")
