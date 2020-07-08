from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('320x480')
window.configure(bg="#282828")

def hello():
    print("hai")
button_1 = Button(window, text ="1",padx=20,pady=20, command = hello)
button_2 = Button(window, text ="2",padx=20,pady=20, command = hello)
button_3 = Button(window, text ="3",padx=20,pady=20, command = hello)
button_1.grid(row=1,column=1)
button_2.grid(row=1,column=2)
button_3.grid(row=1,column=3)
mainloop()