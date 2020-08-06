from sklearn import datasets

iris_data = datasets.load_iris()

#dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])

# size = 150,4
y = iris_data.target

print(iris_data.data.shape)
print(iris_data.target_names)
print(iris_data.DESCR)


