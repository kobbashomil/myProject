#========= calculator python ====
from tkinter import *

#========= def ===================
def click(number):# insert data
     
    global equation_text
    equation_text = equation_text + str(number)
    click_entry.set(equation_text)           
def clear():  # clear screen
    global equation_text
    equation_text=""
    click_entry.set(equation_text)
def equale(): # result opertor
    global equation_text
    try:
       total=eval(equation_text)
       click_entry.set(total)
       #equation_text=total
    except SyntaxError:
        click_entry.set("SystemError")
        #equation_text=""  
    except ZeroDivisionError:
        click_entry.set("arithmetic error")  
        equation_text=""  
#===== window ==========
win= Tk()
win.geometry('300x400')
win.resizable(0,0)
win.title('calculoter')
win.config(bg='#1CA994')
#===== Entry ====
equation_text= ""
click_entry=StringVar()
screen=Entry(win,bd=10,font='arial 21',width=30,
bg='lightgrey',textvariable=click_entry)
screen.pack()
#=========variable ==========


                                     
#==== button ============
n1=Button(win,text='1',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(1))
n1.place(x=10,y=60)
n2=Button(win,text='2',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(2))
n2.place(x=85,y=60)
n3=Button(win,text='3',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(3))
n3.place(x=160,y=60)
n4=Button(win,text='4',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(4))
n4.place(x=10,y=145)
n5=Button(win,text='5',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(5))
n5.place(x=85,y=145)
n6=Button(win,text='6',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(6))
n6.place(x=160,y=145)
n7=Button(win,text='7',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(7))
n7.place(x=10,y=230)
n8=Button(win,text='8',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(8))
n8.place(x=85,y=230)
n9=Button(win,text='9',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(9))
n9.place(x=160,y=230)
n0=Button(win,text='0',font='arial 19 bold',bg='grey',bd=10,padx=10,pady=5,command=lambda:click(0))
n0.place(x=10,y=315)
#========== fx =============
pluse=Button(win,text='+',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=lambda:click('+'))
pluse.place(x=235,y=60)
minus=Button(win,text='-',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=lambda:click('-'))
minus.place(x=235,y=145)
milti=Button(win,text='*',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=lambda:click('*'))
milti.place(x=235,y=230)
div=Button(win,text='/',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=lambda:click('/'))
div.place(x=235,y=315)
eq=Button(win,text='=',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=equale)
eq.place(x=85,y=315)
cl=Button(win,text='c',font='arial 19 bold',bg='orange',bd=10,padx=10,pady=5,command=clear)
cl.place(x=160,y=315)

#========== END =============
win.mainloop()