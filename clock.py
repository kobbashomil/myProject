# ==== import
import turtle
import time
#======= window 
win=turtle.Screen()
win.setup(width=600,height=600)
win.bgcolor("gray")
win.tracer(0)
#========= variable
#h=6
#m=15
#s=37
#=========== creater pin
pen=turtle.Turtle()
pen.penup()
pen.pensize(15)
pen.color('black')
pen.speed(0)
pen.hideturtle()
#=== drawing clock
def clock(h,m,s):
                       
   global pen
   #===== drwing circle
   pen.penup()
   pen.pensize(16)
   pen.setposition(0,210)
   

   pen.setheading(180)
   pen.color ("#1AC994","#F6F6F6")
   pen.pendown()
   pen.begin_fill()
   pen.circle(210)
   pen.end_fill()
   #==== drawing line for hour
   pen.penup()
   pen.setposition(0,0)
   pen.color('black')
   pen.setheading(90)
   for _ in range(12):
            pen.forward(190)
            pen.pendown()
            pen.backward(10) 
            pen.penup()
            pen.setposition(0,0)
            pen.right(360/12)
   
   #====  hand hour
   pen.color('orange')
   pen.pensize(15)
   pen.setheading(90)
   pen.setposition(0,0)
   pen.color('green')
   angle=(h/12) *360
   pen.right(angle)
   pen.pendown()
   pen.forward(100)
   #==== hand minute 
   
   pen.pensize(11)
   pen.setheading(90)
   pen.setposition(0,0)
   angle=(m/60) *360
   pen.right(angle)
   pen.pendown()
   pen.forward(130)
   #=== hand second
   pen.color('blue')
   pen.pensize(13)
   pen.setheading(90)
   pen.setposition(0,0)
   angle=(s/60) *360
   pen.right(angle)
   pen.pendown()
   pen.forward(150)
#=== timezone
while True:
    h = int(time.strftime("%I"))  # gives us the Hours from 0 -to- 12
    m = int(time.strftime("%M"))  # gives us the Minutes
    s = int(time.strftime("%S"))  # gives us the Seconds

#====
pen.clear()
time.sleep(1)
clock(h,m,s)
win.update()
#========  end ==

win.mainloop()