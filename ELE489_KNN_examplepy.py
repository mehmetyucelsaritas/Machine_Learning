import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Visualize some data points
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
plt.scatter(x, y, c=classes)
plt.show()

# turn the input features into a set of points:
# zip function creates an iterator that will aggregate elements from two or more iterables
data = list(zip(x, y))

# Using the input features and target class, 
# we fit(train) a KNN model on the model using 1 nearest neighbor:
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

# test the algorithm on unforeseen data points.
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()


# We fit(train) a KNN model on the model using 5 nearest neighbor:
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)

prediction = knn.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()