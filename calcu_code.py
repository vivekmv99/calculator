from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('320x480')
window.configure(bg="#282828")

# escreen = Entry(window, width=35)
# escreen.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

Text_dis = Text(window, width=40,height=10).place(x=0,y=12)



def hello():
    print("hai")


Button(window, text=" 1 ", height=4,width=10,fg="black").place(x=0,y=200)
Button(window, text=" 2 ", height=4,width=10,fg="black").place(x=90,y=200)
Button(window, text=" 3 ", height=4,width=10,fg="black").place(x=180,y=200)
Button(window, text=" + ", height=4,width=5,fg="black").place(x=270,y=200)
Button(window, text=" 4 ", height=4,width=10,fg="black").place(x=0,y=280)
Button(window, text=" 5 ", height=4,width=10,fg="black").place(x=90,y=280)
Button(window, text=" 6 ", height=4,width=10,fg="black").place(x=180,y=280)
Button(window, text=" - ", height=4,width=5,fg="black").place(x=270,y=280)
Button(window, text=" 7 ", height=4,width=10,fg="black").place(x=0,y=360)
Button(window, text=" 8 ", height=4,width=10,fg="black").place(x=90,y=360)
Button(window, text=" 9 ", height=4,width=10,fg="black").place(x=180,y=360)
Button(window, text=" x ", height=4,width=5,fg="black").place(x=270,y=360)
Button(window, text=" 0 ", height=1,width=10,fg="black").place(x=0,y=440)
Button(window, text=" . ", height=1,width=10,fg="black").place(x=90,y=440)
Button(window, text=" = ", height=1,width=10,fg="black").place(x=180,y=440)
Button(window, text=" / ", height=1,width=5,fg="black").place(x=270,y=440)

mainloop()