from tkinter import *
from tkinter.font import *



window = Tk()
window.title("Calculator")
window.geometry('320x480')
window.configure(bg="#282828")


# Text_dis = Text(window, width=35,height=5).place(x=15,y=12)
# Text_result=Text(window, width=35,height=5,).place(x=15,y=99)

myfont_screen = Font(family="verdana",size="40")
dis_entry = Entry(window,width=8,font=myfont_screen)
dis_entry.place(x=20,y=30)

dis_result = Entry(window,width=8,font=myfont_screen)
dis_result.place(x=20,y=105)
def hello():
    print("hai")




myfont = Font(family="verdana",size="12")

Button(window, text=" √ ", height=3,bg="#668cff",width=6,fg="black",font=myfont).place(x=10,y=196)
Button(window, text=" <- ", height=3,bg="#668cff",width=7,fg="black",font=myfont).place(x=80,y=196)
Button(window, text=" / ", height=3,bg="#668cff",width=7,fg="black",font=myfont).place(x=160,y=196)
Button(window, text=" × ", height=3,bg="#668cff",width=6,fg="black",font=myfont).place(x=240,y=196)
Button(window, text=" 7 ", height=3,bg="gray46",width=6,fg="black",font=myfont).place(x=10,y=253)
Button(window, text=" 8 ", height=3,bg="gray46",width=7,fg="black",font=myfont).place(x=80,y=253)
Button(window, text=" 9 ", height=3,bg="gray46",width=7,fg="black",font=myfont).place(x=160,y=253)
Button(window, text=" + ", height=3,width=6,bg="#668cff",fg="black",font=myfont).place(x=240,y=253)
Button(window, text=" 4 ", height=3,bg="gray46",width=6,fg="black",font=myfont).place(x=10,y=310)
Button(window, text=" 5 ", height=3,bg="gray46",width=7,fg="black",font=myfont).place(x=80,y=310)
Button(window, text=" 6 ", height=3,bg="gray46",width=7,fg="black",font=myfont).place(x=160,y=310)
Button(window, text=" - ", height=3,width=6,bg="#668cff",fg="black",font=myfont).place(x=240,y=310)
Button(window, text=" 1 ", height=3,width=6,bg="gray46",fg="black",font=myfont).place(x=10,y=367)
Button(window, text=" 2 ", height=3,width=7,bg="gray46",fg="black",font=myfont).place(x=80,y=367)
Button(window, text=" 3 ", height=3,width=7,bg="gray46",fg="black",font=myfont).place(x=160,y=367)
Button(window, text=" 0 ", height=2,width=6,bg="gray46",fg="black",font=myfont).place(x=10,y=424)
Button(window, text=" . ", height=2,width=7,bg="gray46",fg="black",font=myfont).place(x=80,y=424)
Button(window, text=" del ",height=2,width=7,bg="orange red",fg="black",font=myfont).place(x=160,y=424)
Button(window, text=" = ", height=5,width=6,bg="gold",fg="black",font=myfont).place(x=240,y=369)

mainloop()