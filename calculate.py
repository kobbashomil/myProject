from tkinter import *
#========= window =========
win=Tk()
win.geometry('300x450+200+200')
win.config(background='#1CA994')

#========== Entry ===========
count=Entry(win,bg='orange',font=('',14,''))
count.pack()
#===============Button =================
no1=Button(win,width='3',height='2',text='1',font=('',14,''),bg='yellow',set)
no1.place(x=10,y=150)
no2=Button(win,width='3',height='2',text='2',font=('',14,''),bg='yellow')
no2.place(x=55,y=150)
no3=Button(win,width='3',height='2',text='3',font=('',14,''),bg='yellow')
no3.place(x=100,y=150)
no4=Button(win,width='3',height='2',text='4',font=('',14,''),bg='yellow')
no4.place(x=145,y=150)
no5=Button(win,width='3',height='2',text='5',font=('',14,''),bg='yellow')
no5.place(x=190,y=150)
no6=Button(win,width='3',height='2',text='6',font=('',14,''),bg='yellow')
no6.place(x=10,y=213)
no7=Button(win,width='3',height='2',text='7',font=('',14,''),bg='yellow')
no7.place(x=55,y=213)
no8=Button(win,width='3',height='2',text='8',font=('',14,''),bg='yellow')
no8.place(x=100,y=213)
no9=Button(win,width='3',height='2',text='9',font=('',14,''),bg='yellow')
no9.place(x=145,y=213)
no0=Button(win,width='3',height='2',text='0',font=('',14,''),bg='yellow')
no0.place(x=190,y=213)
#========= FX =================
pluse=Button(win,width='3',height='2',text='+',font=('',14,''),bg='red')
pluse.place(x=235,y=151)
minuse=Button(win,width='3',height='2',text='-',font=('',14,''),bg='red')
minuse.place(x=235,y=214)
mltple=Button(win,width='3',height='2',text='x',font=('',14,''),bg='red')
mltple.place(x=235,y=277)
div=Button(win,width='3',height='2',text='/',font=('',14,''),bg='red')
div.place(x=235,y=342)
#========== floot=============
point=Button(win,width='5',height='5',text='.',font=('',14,''),bg='red')
point.place(x=168,y=276)
#============ equale ================
point=Button(win,width='8',height='3',text='=',font=('',22,''),bg='red')
point.place(x=10,y=276)


#========== END =============
win.mainloop()