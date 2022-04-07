from tkinter import *

root = Tk()
root.geometry("312x324")
root.resizable(True, True)
root.title("Calculator")


####### functions #######
def btn_click(num):
    # assigning the enter number in inputfield
    global expression
    expression += str(num)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = " "
    input_text.set("")


def equal_press():
    global expression
    total = str(eval(expression))
    input_text.set(total)


def quitter(item):
    global expression
    expression += str(item)
    root.quit()


expression = " "
# StringVar() is used to get instance of input field
input_text = StringVar()

# crearting a frame for calculator
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)
# creating a input field inside frame
input_field = Entry(input_frame, font='arial 18 bold', textvariable=input_text, width=50, bg="#eee", bd=0,
                    relief="sunken")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # ipady= internal padding to increase the hieght of input field

# creating another frame for button inputs

button_frame = Frame(root, width=312, height=272, bg="grey", bd=0)
button_frame.pack()
# first row
clear = Button(button_frame, text="C", fg="black", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_clear())
clear.grid(column=0, row=0)

divide = Button(button_frame, text="/", fg="black", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click(
                    "/"))
divide.grid(column=1, row=0)
equal = Button(button_frame, text="=", fg="black", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
               command=lambda: equal_press())
equal.grid(column=2, row=0)
Exit = Button(button_frame, text="X", fg="black", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
              command=lambda: quitter("X"))
Exit.grid(column=3, row=0)
# #EEE light shade of grey
# second row
button_7 = Button(button_frame, text="7", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("7"))
button_7.grid(row=1)
# fff == white
button_8 = Button(button_frame, text="8", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("8"))
button_8.grid(column=1, row=1)

button_9 = Button(button_frame, text="9", fg="Black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("9"))
button_9.grid(column=2, row=1)
multiply = Button(button_frame, text="*", fg="Black", width=10, height=5, cursor="hand2", bd=0, bg="#eee",
                  command=lambda: btn_click("*"))
multiply.grid(column=3, row=1)

# third row
button_4 = Button(button_frame, text="4", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("4"))
button_4.grid(row=2)
# fff == white
button_5 = Button(button_frame, text="5", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("5"))
button_5.grid(column=1, row=2)

button_6 = Button(button_frame, text="6", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("6"))
button_6.grid(column=2, row=2)
minus = Button(button_frame, text="-", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#eee",
               command=lambda: btn_click("-"))
minus.grid(column=3, row=2)

# 4th row

button_1 = Button(button_frame, text="3", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("3"))
button_1.grid(column=0, row=3)
# fff == white
button_2 = Button(button_frame, text="2", fg="black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("2"))
button_2.grid(column=1, row=3)

button_3 = Button(button_frame, text="1", fg="Black", width=10, height=5, cursor="hand2", bd=0, bg="#fff",
                  command=lambda: btn_click("1"))
button_3.grid(column=2, row=3)
plus = Button(button_frame, text="+", fg="Black", width=10, height=5, cursor="hand2", bd=0, bg="#eee",
              command=lambda: btn_click("+"))
plus.grid(column=3, row=3)
root.mainloop()
