import tkinter as tk
from tkinter import *

window = Tk()
window.title('calculator')
window.geometry('500x500')
window.configure(bg = 'light blue')

expression = ''

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

equation = StringVar()

def clear():
    global expression
    expression = ''
    equation.set(expression)
    expression = ''

def equalpress():
    try:
        global expression
        total = eval(expression)
        equation.set(total)
        expression = ''

    except:
        equation.set('ERROR')
        expression = ''
    
#frame widget
entry_frame = Frame(window)
first_buttons_frame = Frame(window)
second_buttons_frame = Frame(window)
third_buttons_frame = Frame(window)
fourth_buttons_frame = Frame(window)


#entry widget
entry = Entry(entry_frame,width = 34,font = ('DS-Digital',15),borderwidth = 5,textvariable = equation)

#button widget
number7 = Button(first_buttons_frame,text = '7',width = 10,height=5,relief = 'groove',command = lambda:button_click(7))
number8 = Button(first_buttons_frame,text = '8',width = 10,height=5,relief = 'groove',command = lambda:button_click(8))
number9 = Button(first_buttons_frame,text = '9',width = 10,height=5,relief = 'groove',command = lambda:button_click(9))
numberx = Button(first_buttons_frame, text = '*',width = 10,height=5,relief = 'groove',command = lambda:button_click('*'),bg = 'blue')
number4 = Button(second_buttons_frame,text = '4',width = 10,height=5,relief = 'groove',command = lambda:button_click(4))
number5 = Button(second_buttons_frame,text = '5',width = 10,height=5,relief = 'groove',command = lambda:button_click(5))
number6 = Button(second_buttons_frame,text = '6',width = 10,height=5,relief = 'groove',command = lambda:button_click(6))
numberminus = Button(second_buttons_frame,text = '-',width = 10,height=5,relief = 'groove',command = lambda:button_click('-'),bg = 'blue')
number1 = Button(third_buttons_frame, text = '1',width = 10,height=5,relief = 'groove',command = lambda:button_click(1))
number2 = Button(third_buttons_frame, text = '2',width = 10,height=5,relief = 'groove',command = lambda:button_click(2))
number3 = Button(third_buttons_frame, text = '3',width = 10,height=5,relief = 'groove',command = lambda:button_click(3))
numberplus = Button(third_buttons_frame, text = '+',width = 10,height=5,relief = 'groove',command = lambda:button_click('+'),bg = 'blue')
numbernill = Button(fourth_buttons_frame, text = '0',width = 10,height=5,relief = 'groove',command = lambda:button_click(0))
division = Button(fourth_buttons_frame, text = '/',width = 10,height=5,relief = 'groove',command = lambda:button_click('/'))
numberdel = Button(fourth_buttons_frame, text = 'del',width = 10,height=5,relief = 'groove',command = clear)
equals = Button(fourth_buttons_frame,text = '=',width = 10,height=5,relief = 'groove',command = equalpress,bg = 'blue')


#display input and buttons
entry.pack()
number7.pack(side = LEFT)
number8.pack(side= LEFT)
number9.pack(side = LEFT)
numberx.pack(side = LEFT)
number4.pack(side = LEFT)
number5.pack(side = LEFT)
number6.pack(side = LEFT)
numberminus.pack(side = LEFT)
number1.pack(side = LEFT)
number2.pack(side = LEFT)
number3.pack(side = LEFT)
numberplus.pack(side = LEFT)

numbernill.pack(side = LEFT)
division.pack(side = LEFT)
numberdel.pack(side = LEFT)
equals.pack(side = LEFT)

#display frame
entry_frame.pack()
first_buttons_frame.pack()
second_buttons_frame.pack()
third_buttons_frame.pack()
fourth_buttons_frame.pack()


window.mainloop()












