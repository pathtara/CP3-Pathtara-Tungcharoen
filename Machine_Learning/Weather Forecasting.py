import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv
dataset = pd.read_csv('https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv')

#dataset.plot(x = 'MinTemp', y = 'MaxTemp', style = 'o')
#plt.title('Weather')
#plt.xlabel('Min Temp')
#plt.ylabel('Max Temp')
#plt.show()
#print(dataset.describe()) # see pandas table

x = dataset["MinTemp"].values.reshape(-1,1)
y = dataset["MaxTemp"].values.reshape(-1,1)

# trian set : test set = 80 : 20
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


# training algorithm
model = LinearRegression()
model.fit(x_train, y_train)


# test model
y_predict = model.predict(x_test)  # โยนตัวแปรที่ทราบค่า ('x_test')เข้าไปใน Fucntion "Predict" 


# plot regression
#plt.scatter(x_test, y_test)
#plt.plot(x_test, y_predict, color = "red")
#plt.show()

# เทียบข้อมูลจริง กับ ข้อมูลที่พยากรณ์
df = pd.DataFrame({'Actually':y_test.flatten(), 'Predicted':y_predict.flatten()}) 
# DataFrame รองรับเฉพาะ array 1มิติ แต่ตัว y_test และ y_predict จะเป็น array2มิติ ดังนั้นให้ใช้คำสั่ง flatten() ในการแปลงข้อมูล

#df1 = df.head(20)
#df1.plot(figsize=(16,10))
#plt.show()


mae = metrics.mean_absolute_error(y_test, y_predict)
mse = metrics.mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r_square = metrics.r2_score(y_test, y_predict)


print("MAE (Mean Absolute Error) = ", mae)
print("MSE (Mean Squared Error) = ", mse)
print("RMSE (Squared root MSE) = ", rmse)
print("Model Score (R_Square) = ", r_square)