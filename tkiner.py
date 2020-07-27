from tkinter import * 

def say_hello():
    print("Say Helollllll")


def say_bye():
    print("Byeeeeeeeeeeeeeeeeeeeee")


main_window = Tk()
button = Button(main_window, text = "click me", command = say_hello, width=20)
button.place (x = 50, y = 20)
button2 = Button(main_window, text = "Don't click me", command = say_bye)
button2.place (x = 50, y = 100)
label = Label(main_window, text = "Hello", width=20, fg = "blue", bg = "red", font=("Helvetica", 38), anchor = W).grid(row=1, column=2)
main_window.mainloop()
