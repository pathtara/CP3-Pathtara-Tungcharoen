from tkinter import *


def calculate(event):
    height = height_entry.get()
    weight = weight_entry.get()
    bmi = float(weight) / ((float(height)/100)**2)
    print(bmi)
    
    

MainWindow = Tk()
height_box = Label(MainWindow, text = "Height (CM)")
height_box.grid(row = 0, column = 0)
height_entry = Entry(MainWindow)
height_entry.grid(row = 0, column = 1)
weight_box = Label(MainWindow, text = "Weight (KG)")
weight_box.grid(row = 1, column = 0)
weight_entry = Entry(MainWindow)
weight_entry.grid(row = 1, column = 1)
calculation_button = Button(MainWindow, text = "Calculate")
calculation_button.bind('<Button-1>', calculate)
calculation_button.grid(row = 2, column = 0)
bmi_result = Label(MainWindow, text = "")


MainWindow.mainloop()