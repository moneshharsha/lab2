# Importing necessary libraries
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
x=np.array([[1,2,3],[3,4,5],[1,1,1],[9,8,1],[0,7,3]])
y=np.array(['class1','class2','class1','class2','class1'])
k=3
knn=KNeighborsClassifier(k)
knn.fit(x,y)
output=np.array([[0,0,0],[9,9,9]])
print(f"Output class:{knn.predict(output)}")
