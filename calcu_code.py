from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from datetime import date


window = Tk()
window.title("Magic Calculator")
window.geometry('320x480')
window.configure(bg="#282828")
window.resizable(width=False,height=False)

######### entry screen and result screen creation##########

myfont_screen = Font(family="verdana",size="40")
dis_entry = Entry(window,width=8,font=myfont_screen,justify=RIGHT)
dis_entry.place(x=20,y=30)

dis_result = Entry(window,width=8,font=myfont_screen,justify=RIGHT)
dis_result.place(x=20,y=105)

########menu bar creation#############

info_menu = Menu(window)
window.config(menu=info_menu)


########## menu function#############

def abt_info():
    messagebox.showinfo("About","Magic calculator is an ordinary calculator. But\n"
                                "it comes with a Magic button for finding age and\n"
                                "this project is done on the basis of python coding\n"
                                "challenge conducted by CROSSROADS.\n"
                                "I also thank CROSSROADS TEAM especially Nikhil sir\n"
                                "for his wonderful tutorial and inspiring words.\n")
def help_info():
    messagebox.showinfo("Help","1-> Enter the first number. \n"
                               "2-> Enter the operation that you wish to do.\n"
                               "          (+ , - , / , x , √   )\n"
                               "3-> Enter the second number.\n"
                               "4-> Result will displayed on 2nd screen.\n"
                               "**** HOW TO USE MAGIC BUTTON ❤ ****\n"
                               "1-> Enter the year when you are born\n"
                               "2-> And press the magic button ❤\n")

########menu---choice button label##################

help_menu = Menu(info_menu)
info_menu.add_cascade(label=" Help ",menu=help_menu)
help_menu.add_command(label="About ",command=abt_info)
help_menu.add_command(label="Help ",command=help_info)
help_menu.add_command(label="Exit ", command=window.quit)

#################function for button click(0-9)##########################

def button_click(number):
    num = dis_entry.get()
    dis_entry.delete(0,END)
    dis_entry.insert(0,str(num) + str(number))

#############function for delete button#################################

def button_del():
    dis_entry.delete(0,END)
    dis_result.delete(first=0, last=100)

#############function for add button##################################

def add_button():
    try:
        first_number = dis_entry.get()
        global f_num
        global operation
        operation = "addition"
        f_num = int(first_number)
        dis_entry.delete(0, END)
    except:
        dis_entry.insert(0, "ERROR")
        dis_result.insert(0, "→")
        dis_entry.delete(5, END)
        dis_result.delete(1, END)
        messagebox.showinfo("Addition operation",
                            "1-> Enter the first number that you want to  \n"
                            "Add. \n"
                            "2-> After that click the add + button.\n"
                            "3-> Enter the second number that you want Add\n"
                            "with the first number. \n"
                            "Then the result will displayed in your\n"
                            "second screen.")
        dis_entry.delete(0, END)
        dis_result.delete(0, END)

##############function for result(equal-to-button and mathematical-opertions) ##########

def equal_button():
    second_number = dis_entry.get()
    dis_entry.delete(0, END)
    try:
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
    except:
        dis_entry.delete(0, END)
        dis_result.delete(0, END)
        dis_entry.insert(0, "Error")
        dis_result.insert(0, "Error")

#############function for subtration button##################################

def sub_button():
    try:
        first_number = dis_entry.get()
        global f_num
        global operation
        operation = "subtraction"
        f_num = int(first_number)
        dis_entry.delete(0, END)
    except:
        dis_entry.insert(0, "ERROR")
        dis_result.insert(0, "→")
        dis_entry.delete(5, END)
        dis_result.delete(1, END)
        messagebox.showinfo("Subtraction operation",
                            "1-> Enter the first number that you want to  \n"
                            "Subtract. \n"
                            "2-> After that click the subtract - button.\n"
                            "3-> Enter the second number that you want subtract\n"
                            "with the first number. \n"
                            "Then the result will displayed in your\n"
                            "second screen.")
        dis_entry.delete(0, END)
        dis_result.delete(0, END)

#############function for divide-button##################################

def div_button():
    try:
        first_number = dis_entry.get()
        global f_num
        global operation
        operation= "division"
        f_num=int(first_number)
        dis_entry.delete(0,END)
    except:
        dis_entry.insert(0, "ERROR")
        dis_result.insert(0, "→")
        dis_entry.delete(5, END)
        dis_result.delete(1, END)
        messagebox.showinfo("Division operation",
                            "1-> Enter the first number that you want to  \n"
                            "Divide. \n"
                            "2-> After that click the divide / button.\n"
                            "3-> Enter the second number that you want divide\n"
                            "with the first number. \n"
                            "Then the result will displayed in your\n"
                            "second screen.")
        dis_entry.delete(0, END)
        dis_result.delete(0, END)

#############function for Multiplication button##################################

def mul_button():
    try:
        first_number = dis_entry.get()
        global f_num
        global operation
        operation = "multiplication"
        f_num=int(first_number)
        dis_entry.delete(0,END)
    except:
        dis_entry.insert(0, "ERROR")
        dis_result.insert(0, "→")
        dis_entry.delete(5, END)
        dis_result.delete(1, END)
        messagebox.showinfo("Multiplication operation",
                            "1-> Enter the first number that you want to  \n"
                            "Multiply. \n"
                            "2-> After that click the Multiply x button.\n"
                            "3-> Enter the second number that you want multiply\n"
                            "with the first number. \n"
                            "Then the result will displayed in your\n"
                            "second screen.")
        dis_entry.delete(0, END)
        dis_result.delete(0, END)

#############function for Square root button##################################

def square_bttn():
    try:
        first_number = dis_entry.get()
        global f_num
        global operation
        operation = "square root"
        f_num = int(first_number)
        dis_entry.delete(0, END)
    except:
        dis_entry.insert(0, "ERROR")
        dis_result.insert(0, "→")
        dis_entry.delete(5, END)
        dis_result.delete(1, END)
        messagebox.showinfo("Square root operation",
                            "1-> Enter the number that you want find \n"
                            "the root of. \n"
                            "2-> After that click the root √ button.\n"
                            "Then the result will displayed in your\n"
                            "second screen.")
        dis_entry.delete(0, END)
        dis_result.delete(0, END)

#########function for magic button and operation############################

def magic_button():
    try:
        first_numberr = dis_entry.get()
        f_numm = int(first_numberr)
        today = date.today()
        yr = today.year
        dis_entry.delete(0, END)
        if f_numm != 0:
            dis_entry.insert(0, "AGE")
            dis_result.insert(0, int(yr) - int(f_numm))
            dis_entry.delete(3, END)
        else:
            second_number = dis_entry.get()
            dis_result.insert(0, "ERROR")
    except:
        messagebox.showinfo("Magic operation","**** HOW TO USE MAGIC BUTTON ❤ ****\n"
                                    "1-> Enter the year when you are born\n"
                                    "2-> And press the magic button ❤\n"
                                    "Then Your Age will displayed in your\n"
                                    "second screen.")

##########################################################################################
#########################BUTTON/DESIGN/LAYOUT/Font########################################
##########################################################################################

myfont = Font(family="verdana",size="12")
Button(window, text=" √ ", height=3,bg="#668cff",width=6,fg="black",font=myfont,command=square_bttn).place(x=10,y=196)
Button(window, text=" ❤ ", height=3,bg="#668cff",width=7,fg="black",font=myfont,command=magic_button).place(x=80,y=196)
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
##################################################################################################################

##############pre-defined method used when application is ready to run##################

mainloop()

########################################################################################
