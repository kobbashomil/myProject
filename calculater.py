from tkinter import *
import time
root= Tk()
root.geometry('450x600+200+200')
root.config(background='#1CA994')

number1=StringVar()
number2=StringVar()
number3=StringVar()
number4=StringVar()
number5=StringVar()

def get_time():
    ct=time.ctime()
    return ct

citytime =Label(root,font=('times',15,'bold'),text=get_time())
citytime.place(x=120,y=15)

#================================def===================================
def calculate():
   n1=float(number1.get())
   c1=n1/3
   c2=n1*1.5
   c3=n1*1.3
   c4=n1*1.1
   number2.set(c1)
   number3.set(c2)
   number4.set(c3)
   number5.set(c4)
   
   



#===================== current========================================
current=Label(root,font=('times',15,'bold'),text='current',bg='#1CA994')
current.place(x=40,y=100)

value1=Entry(root,font=('times',15,'bold'),bd=4,bg='yellow',textvariable=number1)
value1.place(x=200,y=100)

#========================================SizeWire=======================
SizeWire=Label(root,font=('times',15,'bold'),text='SizeWire',bg='#1CA994')
SizeWire.place(x=40,y=150)


value2=Entry(root,font=('times',15,'bold'),bd=4,bg='yellow',textvariable=number2)
value2.place(x=200,y=150)

#===============================CurrentContactor====================================
CurrentContactor=Label(root,font=('times',15,'bold'),text='currentContactor',bg='#1CA994')
CurrentContactor.place(x=40,y=200)



value3=Entry(root,font=('times',15,'bold'),bd=4,bg='yellow',textvariable=number3)
value3.place(x=200,y=200)



#==========================CircuitBreaker=========================================

circuitBrecker=Label(root,font=('times',15,'bold'),text='circuitBrecker',bg='#1CA994')
circuitBrecker.place(x=40,y=250)



value4=Entry(root,font=('times',15,'bold'),bd=4,bg='yellow',textvariable=number4)
value4.place(x=200,y=250)


#=========================CurrentOverLoad============================================

CurrentOverLoad=Label(root,font=('times',15,'bold'),text='CurrentOverLoad',bg='#1CA994')
CurrentOverLoad.place(x=40,y=300)




value5=Entry(root,font=('times',15,'bold'),bd=4,bg='yellow',textvariable=number5)
value5.place(x=200,y=300)


#=====================================buttom====================================

Butt=Button(root,width=8,padx=2,pady=2,bd=4,text='calculate',command=calculate )
Butt.place(x=200,y=400) 




root.mainloop()