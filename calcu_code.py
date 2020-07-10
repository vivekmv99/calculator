from tkinter import *
from tkinter.font import *



window = Tk()
window.title("Calculator")
window.geometry('320x480')
window.configure(bg="#282828")


# Text_dis = Text(window, width=35,height=5).place(x=15,y=12)
# Text_result=Text(window, width=35,height=5,).place(x=15,y=99)

myfont_screen = Font(family="verdana",size="40")
dis_entry = Entry(window,width=8,font=myfont_screen,justify=RIGHT)
dis_entry.place(x=20,y=30)

dis_result = Entry(window,width=8,font=myfont_screen,justify=RIGHT)
dis_result.place(x=20,y=105)


def button_click(number):
    num = dis_entry.get()
    dis_entry.delete(0,END)
    dis_entry.insert(0,str(num) + str(number))

def button_del():
    dis_entry.delete(0,END)

def back_space():
    dis_entry.delete(0,1)


def add_button():
    first_number = dis_entry.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_number)
    dis_entry.delete(0, END)

def equal_button():
    second_number = dis_entry.get()
    dis_entry.delete(0, END)
    if operation == "addition":
        dis_entry.insert(0, str(f_num) + "+" + str(second_number) + "=")
        dis_result.insert(0, int(f_num) + int(second_number))
    elif operation == "subtraction":
        dis_entry.insert(0, str(f_num) + "-" + str(second_number) + "=")
        dis_result.insert(0, int(f_num) - int(second_number))
    elif operation == "division":
        dis_entry.insert(0, str(f_num) + "/" + str(second_number) + "=")
        dis_result.insert(0, int(f_num) / int(second_number))
    elif operation == "multiplication":
        dis_entry.insert(0, str(f_num) + "x" + str(second_number) + "=")
        dis_result.insert(0, int(f_num) * int(second_number))
    elif operation == "square root":
        dis_entry.insert(0, "√" + str(f_num))
        dis_result.insert(0, int(f_num) ** 0.5)
    else:
        dis_result.insert(0, "Error")

def sub_button():
    first_number = dis_entry.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    dis_entry.delete(0, END)
def div_button():
    first_number = dis_entry.get()
    global f_num
    global operation
    operation= "division"
    f_num=int(first_number)
    dis_entry.delete(0,END)

def mul_button():
    first_number = dis_entry.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num=int(first_number)
    dis_entry.delete(0,END)


def square_bttn():
    first_number = dis_entry.get()
    global f_num
    global operation
    operation = "square root"
    f_num = int(first_number)
    dis_entry.delete(0, END)

myfont = Font(family="verdana",size="12")
Button(window, text=" √ ", height=3,bg="#668cff",width=6,fg="black",font=myfont,command=square_bttn).place(x=10,y=196)
Button(window, text=" <- ", height=3,bg="#668cff",width=7,fg="black",font=myfont,command=back_space).place(x=80,y=196)
Button(window, text=" / ", height=3,bg="#668cff",width=7,fg="black",font=myfont,command=div_button).place(x=160,y=196)
Button(window, text=" × ", height=3,bg="#668cff",width=6,fg="black",font=myfont,command=mul_button).place(x=240,y=196)
Button(window, text=" 7 ", height=3,bg="gray46",width=6,fg="black",font=myfont,command=lambda:button_click(7)).place(x=10,y=253)
Button(window, text=" 8 ", height=3,bg="gray46",width=7,fg="black",font=myfont,command=lambda:button_click(8)).place(x=80,y=253)
Button(window, text=" 9 ", height=3,bg="gray46",width=7,fg="black",font=myfont,command=lambda:button_click(9)).place(x=160,y=253)
Button(window, text=" + ", height=3,width=6,bg="#668cff",fg="black",font=myfont,command=add_button).place(x=240,y=253)
Button(window, text=" 4 ", height=3,bg="gray46",width=6,fg="black",font=myfont,command=lambda:button_click(4)).place(x=10,y=310)
Button(window, text=" 5 ", height=3,bg="gray46",width=7,fg="black",font=myfont,command=lambda:button_click(5)).place(x=80,y=310)
Button(window, text=" 6 ", height=3,bg="gray46",width=7,fg="black",font=myfont,command=lambda:button_click(6)).place(x=160,y=310)
Button(window, text=" - ", height=3,width=6,bg="#668cff",fg="black",font=myfont,command=sub_button).place(x=240,y=310)
Button(window, text=" 1 ", height=3,width=6,bg="gray46",fg="black",font=myfont,command=lambda:button_click(1)).place(x=10,y=367)
Button(window, text=" 2 ", height=3,width=7,bg="gray46",fg="black",font=myfont,command=lambda:button_click(2)).place(x=80,y=367)
Button(window, text=" 3 ", height=3,width=7,bg="gray46",fg="black",font=myfont,command=lambda:button_click(3)).place(x=160,y=367)
Button(window, text=" 0 ", height=2,width=6,bg="gray46",fg="black",font=myfont,command=lambda:button_click(0)).place(x=10,y=424)
Button(window, text=" 00 ", height=2,width=7,bg="gray46",fg="black",font=myfont,command=lambda:button_click("00")).place(x=80,y=424)
Button(window, text=" del",height=2,width=7,bg="orange red",fg="black",font=myfont,command=button_del).place(x=160,y=424)
Button(window, text=" = ", height=5,width=6,bg="gold",fg="black",font=myfont,command=equal_button).place(x=240,y=369)

mainloop()