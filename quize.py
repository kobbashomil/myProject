#======== python calculator ===
from tkinter import *
#=========== def ============
def button_press(num):
    global equation_text
    equation_text=equation_text + str(num)  
    equation_text.set=lab_text  
    equation_text=""             

    
#========= window ===========
window=Tk()
window.geometry("400x500")
window.title("calculator")


#========= entry ===========
#equation_text=StringVar()

Label=Entry(window,width=30,bg='lightgrey',font='arial 21',bd=5,textvariable=lab_text)
Label.pack()
#========= BUTTON =============
frame = Frame(window)
frame.pack()
lab_text=StringVar()
equation_text=""
button1 = Button(frame, text=1, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button1.grid(row=1, column=1)
button2 = Button(frame, text=2, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(2))
button2.grid(row=1, column=2)
button3 = Button(frame, text=3, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(3))
button3.grid(row=1, column=3)
button4 = Button(frame, text= '+' , height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(4))
button4.grid(row=1, column=4)
button5 = Button(frame, text=4, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button5.grid(row=2, column=1)
button6 = Button(frame, text=5, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button6.grid(row=2, column=2)
button7 = Button(frame, text=6, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button7.grid(row=2, column=3)
button8 = Button(frame, text='-', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(1))
button8.grid(row=2, column=4)
button9 = Button(frame, text=7, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button9.grid(row=3, column=1)
button0 = Button(frame, text=8, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button0.grid(row=3, column=2)
button0 = Button(frame, text=9, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button0.grid(row=3, column=3)
button0 = Button(frame, text='/', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(1))
button0.grid(row=3, column=4)
button0 = Button(frame, text=0, height=3, width=4,bd=4, font=35,bg='orange',
                 command=lambda: button_press(1))
button0.grid(row=4, column=1)
button0 = Button(frame, text='=', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(1))
button0.grid(row=4, column=2)
button0 = Button(frame, text='C', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(1))
button0.grid(row=4, column=3)
button0 = Button(frame, text='*', height=3, width=4,bd=4, font=35,bg='gray',
                 command=lambda: button_press(1))
button0.grid(row=4, column=4)












#====== END ============
window.mainloop()