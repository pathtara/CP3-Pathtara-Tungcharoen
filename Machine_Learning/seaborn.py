import seaborn as sb
iris_dataset = sb.load_dataset('iris')
print(iris_dataset.head())

sb.set()
sb.pairplot(iris_dataset, hue = 'species', height = 2)

