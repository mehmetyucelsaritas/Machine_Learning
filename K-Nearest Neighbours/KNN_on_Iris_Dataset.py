from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# classes --> 1:Iris Setosa 2:Iris Versicolor
# features --> 1: Sepal Length 2: Sepal Width

# import iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=np.c_[iris["data"], iris["target"]], columns=iris["feature_names"] + ["target"])

# drop unwanted data and features
iris_df = iris_df.drop(columns=["petal width (cm)", "petal length (cm)"])

# shufle dataframe
iris_df = iris_df.sample(frac=1)

# subset rows
iris_df = iris_df[iris_df["target"] < 2]

plt.scatter(iris_df["sepal width (cm)"], iris_df["sepal length (cm)"], c=iris_df["target"])
plt.xlabel("sepal width (cm)")
plt.ylabel("sepal length (cm)")
plt.show()

# Divide the classes into train and test sets
train_df = iris_df[:80]
test_df = iris_df[80:]
train_data = list(zip(tuple(train_df["sepal width (cm)"]), tuple(train_df["sepal length (cm)"])))
test_data = list(zip(tuple(test_df["sepal width (cm)"]), tuple(test_df["sepal length (cm)"])))
classes = list(train_df["target"])

# initialize knn
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_data, classes)

prediction = knn.predict(test_data)

accuracy = accuracy_score(list(test_df["target"]), list(prediction))
print(accuracy)
print(iris_df.tail())
print(iris_df.describe())
