from sklearn import datasets
from sklearn.model_selection import train_test_split


iris_datasets = datasets.load_iris()

# iris_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])

# x_train, x_test, y_train, y_test = train_test_split(iris_datasets['data'], iris_datasets['target']) >>> can set like this
# size = 150
# train 80% = 120
# test 20% = 30
x_train, x_test = train_test_split(iris_datasets['data'], train_size = 0.8, test_size = 0.2, random_state = 0)  # default = 75:25
y_train, y_test = train_test_split(iris_datasets['target'], train_size = 0.8, test_size = 0.2, random_state = 0)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

  