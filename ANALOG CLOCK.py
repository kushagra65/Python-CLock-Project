#import the essential modules
import time# importing the time module
import turtle #importing the turtle module from the LOGO days
#----------------------------------------------------------------

#creating the screen of the clock
wn = turtle.Screen()#creating a screen
wn.bgcolor("black")#setting the backgroung color
wn.setup(width=600, height=600)#setting the size of the screen
wn.title("analog clock @ kushagra verma")
wn.tracer(0)#sets the animation time ,see in the while loop
#---------------------------------------------------------------------------

#creating our drawing pen
pen = turtle.Turtle()# create  objects
pen.hideturtle()
pen.speed(0)  # animation speed
pen.pensize(5)  # widht of the pens the pen is drawing


def DrawC(h,m,s,pen):# creates min,hr,sec hands

    #drawing a clock face
    pen.penup()  #means dont draw a  line
    pen.goto(0, 210)
    pen.setheading(180)#pen facing to the left
    pen.color("orange")#color of the circle
    pen.pendown()
    pen.circle(210)

    #now drawing lines for the hours
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    # Drawing the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #drawing the minite hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle=( m / 60 ) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Drawing the sec hand
    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)
    angle=( s / 60 ) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:

    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))

    DrawC(h,m,s,pen)
    wn.update()
    time.sleep(1)
    pen.clear()
#after exiting the loop a error will show ignore the error