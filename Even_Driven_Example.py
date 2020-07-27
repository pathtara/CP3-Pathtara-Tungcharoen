from tkinter import *

def left_click(event):
    print("left click")

def right_click(event):
    print("right click")


main = Tk()
button = Button(main, text = "Hello Test")
button.pack()
button.bind('<Button-1>', left_click)
button.bind('<Button-3>', right_click)
main.mainloop()