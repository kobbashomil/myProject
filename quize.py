#======== python calculator ===
from tkinter import *
#=========== def ============
def button_press(num):
    global equation_text
    equation_text=equation_text + str(num)  
    lab_text.set( equation_text) 
    #equation_text=""             
def clear_text():
    global equation_text
    lab_text.set("")
    equation_text=""
def equal():
    global equation_text
    lab_text.set(eval(equation_text))
    equation_text=""

    
#========= window ===========
window=Tk()
window.geometry("400x500")
window.title("calculator")
window.resizable(0,0)

#========= entry ===========
equation_text=""
lab_text=StringVar()

screen=Entry(window,bd=10,font='arial 21',width=30,
bg='lightgrey',textvariable=lab_text)
screen.pack()
#========= BUTTON =============
frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button1.grid(row=1, column=1)
button2 = Button(frame, text=2, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(2))
button2.grid(row=1, column=2)
button3 = Button(frame, text=3, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(3))
button3.grid(row=1, column=3)


plus= Button(frame, text= '+' , height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press('+'))
plus.grid(row=1, column=4)


button4 = Button(frame, text=4, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(4))
button4.grid(row=2, column=1)
button5 = Button(frame, text=5, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(5))
button5.grid(row=2, column=2)
button6 = Button(frame, text=6, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(6))
button6.grid(row=2, column=3)


minus = Button(frame, text='-', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press('-'))
minus.grid(row=2, column=4)


button7 = Button(frame, text=7, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(7))
button7.grid(row=3, column=1)
button8 = Button(frame, text=8, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(8))
button8.grid(row=3, column=2)
button9 = Button(frame, text=9, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(9))
button9.grid(row=3, column=3)


div = Button(frame, text='/', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press('/'))
div.grid(row=3, column=4)



button0 = Button(frame, text=0, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(0))
button0.grid(row=4, column=1)


equal = Button(frame, text='=', height=3, width=4,bd=4, font=35,bg='gray',
                 command=equal)
equal.grid(row=4, column=2)
clear = Button(frame, text='C', height=3, width=4,bd=4, font=35,bg='gray',
                 command= clear_text)
clear.grid(row=4, column=3)
milti = Button(frame, text='*', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press('*'))
milti.grid(row=4, column=4)












#====== END ============
window.mainloop()