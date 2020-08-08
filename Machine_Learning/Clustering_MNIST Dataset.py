import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score


def display_image(x):
    plt.imshow(
    x.reshape(28,28),
    cmap=plt.cm.binary,
    interpolation='nearest'
    )
    plt.show()

def display_prediction(clf, actually_y, x):
    print("Actually = ", actually_y)
    print("Prediction = ", clf.predict([x])[0])

mnist_raw = loadmat('Machine_Learning\mnist-original.mat')
mnist = {
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}


x = mnist['data']
y = mnist['target']

# train an test dataset
# แบ่งข้อมูลออกเป็น Class 0-9
x_train, x_test, y_train, y_test = x[:60000], x[:60000], y[:60000], y[:60000]


# แบ่งข้อมูลออกเป็น 2 ชุดว่าอยู่ใน Class 0 หรือ Class ที่ไม่ใช่ 0 (Biary Classification) 
# if Class 0 > return True
# if not Class 0 > return False
# ตรวจสอบว่าข้อมูลตำแหน่งที่ 5,000 เป็นเลข 0 หรือไม่
# y_train = [0, 0, 0,....,9, 9, 9]
# >>>  y_train_0 = [True, True, True,..., False, False, False]
predict_position = 5000
y_train_0 = (y_train == 0) # เปลี่ยน int ใน array ให้กลายเป็น boolean
y_test_0 = (y_test == 0)

print(y_test[predict_position])
print(y_test_0[predict_position])

# สร้าง Model
# ใช้ y_train_0(หรือเลขที่ต้องการใช้) จากการทำ Binary Classification ในการ training ข้อมูล (True / False)
# ถ้าใช้ y_train จะเป็นการ training เลขทุกตัวตั้งแต่ 0-9
sgd_clf = SGDClassifier()
sgd_clf.fit(x_train, y_train_0) 
# display_prediction(sgd_clf, y_test_0[predict_position], x_test[predict_position])
# display_image(x_test[predict_position])


# การวัดประสิทธิภาพ Model
# 1.Cross Validation Test 
# แบ่งข้อมูลออกเป็น k ส่วน และทำการทดลอง k ครั้ง ดูว่าการรัน Model ในแต่ละครั้งให้ผลลัพธ์เหมือนกันหรือไม่
score = cross_val_score(sgd_clf, x_train, y_train_0, cv=3, scoring="accuracy")
print(score)
