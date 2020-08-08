# import pylab
# import matplotlib.pyplot as plt
# from sklearn import datasets
# digit_dataset = datasets.load_digits()
# # dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])

# print(digit_dataset.images[0].shape)
# print(digit_dataset.images[0])

# # pylab.imshow(digit_dataset.images[4], cmap=pylab.cm.gray_r)  # ใช้ loop ในกรณีที่ต้องการให้แสดงหลายรูป
# # pylab.show()


# plt.imshow(digit_dataset.images[4], cmap=plt.get_cmap('gray'))  # ใช้ loop ในกรณีที่ต้องการให้แสดงหลายรูป
# plt.show()

#########################################################
# Load original MNIST Data Set
from scipy.io import loadmat
import matplotlib.pyplot as plt


mnist_raw = loadmat('Machine_Learning\mnist-original.mat')

mnist = {
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

x = mnist['data']
y = mnist['target']

no = int(input("Number : "))


number = x[no]
number_image = number.reshape(28,28)


print(y[no])
plt.imshow(
    number_image,
    cmap=plt.cm.binary,
    interpolation="nearest"
    )
plt.show()