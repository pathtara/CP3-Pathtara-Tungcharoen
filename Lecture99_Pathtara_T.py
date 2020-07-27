from tkinter import *


def calculate(event):
    height = height_entry.get()
    weight = weight_entry.get()
    bmi = round(float(weight) / ((float(height)/100)**2), 2)
    if bmi < 18.5:
        bmi_2 = "อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม"
    elif 18.5 <= bmi < 24.9:
        bmi_2 = "อยู่ในเกณฑ์ปกติ"
    elif bmi >= 24.9:
        bmi_2 = "น้ำหนักเกิน"

    bmi_result.configure(text = bmi)
    bmi2_result.configure(text = bmi_2)

    
    

MainWindow = Tk()
height_box = Label(MainWindow, text = "Height (CM)")
height_box.grid(row = 0, column = 0)
height_entry = Entry(MainWindow, anchor = c)
height_entry.grid(row = 0, column = 1)
weight_box = Label(MainWindow, text = "Weight (KG)")
weight_box.grid(row = 1, column = 0)
weight_entry = Entry(MainWindow)
weight_entry.grid(row = 1, column = 1)
calculation_button = Button(MainWindow, text = "Calculate")
calculation_button.bind('<Button-1>', calculate)
calculation_button.grid(row = 2, column = 0)
bmi_result = Label(MainWindow, text = "Result")
bmi_result.grid(row=2, column=1)
bmi2_result = Label(MainWindow, text = "")
bmi2_result.grid(row=3, column=1)


MainWindow.mainloop()