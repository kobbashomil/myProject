import webbrowser
import tkinter as tk
# === window ===

root=tk.Tk()
root.geometry('300x300')
#=== entery ======
blank=tk.Entry(root,font=('',14,''))
blank.pack()
#============ def ============
def search():
     s=blank.get()   
     webbrowser.open(s)              

#==== bottom =====
B=tk.Button(root,text='search',font=('',14,''),command=search)
B.pack()


root.mainloop()