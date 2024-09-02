from math import sin,pi
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.shape("turtle")
wn.bgcolor("lavender blush")
t.speed(10)

colors =["red","deep pink","light pink","dodger blue",]

def color(iteration):
    t.pencolor(colors[iteration % len(colors)])

def at(x,y):
    t.penup()
    t.home()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()

def heart(size,shape):
    t.pensize(5)
    radius = size* sin(shape* pi/180)/(1+ sin((90-shape)* pi/180))
    t.right(shape)
    t.forward(size)
    t.circle(radius,180+ shape)
    t.right(180)
    t.circle(radius, 180+ shape)
    t.forward(size)
    t.left(180-shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1,14):
        color(iteration)
        at(0,iteration* -5)
        heart(iteration*10,45)

hearts() 

import turtle

def draw_heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90,200)
    turtle.setheading(60)
    turtle.circle(-90,200)
    turtle.fillcolor('red')
    turtle.end_fill()

def write_text():
    turtle.up()    
    turtle.setpos(-50,70)    
    turtle.down()    
    turtle.color('white')    
    turtle.write("I Love You ",font=("Arial",16,"bold"))

def main():
    turtle.speed(2)        
    turtle.bgcolor('black')        
    turtle.setup(600,600)        
    turtle.pensize(2)
    draw_heart()        
    write_text()        
    turtle.hideturtle()        
    turtle.done()  

if __name__ == "__main__":
    main()          


