from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('320x480')
window.configure(bg="#282828")

# escreen = Entry(window, width=35)
# escreen.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

Text_dis = Text(window, width=35,height=5).place(x=15,y=12)
Text_result=Text(window, width=35,height=5,).place(x=15,y=99)



def hello():
    print("hai")




Button(window, text=" 7 ", height=3,bg="gray46",width=6,fg="black").place(x=10,y=253)
Button(window, text=" 8 ", height=3,bg="gray46",width=7,fg="black").place(x=80,y=253)
Button(window, text=" 9 ", height=3,bg="gray46",width=7,fg="black").place(x=160,y=253)
Button(window, text=" + ", height=3,width=6,bg="gray46",fg="black").place(x=240,y=253)
Button(window, text=" 4 ", height=3,bg="gray46",width=6,fg="black").place(x=10,y=310)
Button(window, text=" 5 ", height=3,bg="gray46",width=7,fg="black").place(x=80,y=310)
Button(window, text=" 6 ", height=3,bg="gray46",width=7,fg="black").place(x=160,y=310)
Button(window, text=" - ", height=3,width=6,bg="gray46",fg="black").place(x=240,y=310)
Button(window, text=" 1 ", height=3,width=6,bg="gray46",fg="black").place(x=10,y=367)
Button(window, text=" 2 ", height=3,width=7,bg="gray46",fg="black").place(x=80,y=367)
Button(window, text=" 3 ", height=3,width=7,bg="gray46",fg="black").place(x=160,y=367)
Button(window, text=" 0 ", height=2,width=6,bg="gray46",fg="black").place(x=10,y=424)
Button(window, text=" . ", height=2,width=7,bg="gray46",fg="black").place(x=80,y=424)
Button(window, text=" del ", height=2,width=7,bg="red",fg="black").place(x=160,y=424)
Button(window, text=" * ", height=3,width=6,bg="gray46",fg="black").place(x=240,y=369)
Button(window, text=" = ", height=2,width=6,bg="yellow",fg="black").place(x=240,y=424)

mainloop()