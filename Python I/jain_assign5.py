### Assignment 5: Draw Figures
### Author: Niyati Jain
### Program to draw figures in Python using libraries
#!/usr/bin/env python3
import turtle
import random as random  #import using as
from math import sin, cos  #import using from
def main():
    """Main entry point for the flower drawing program."""
    # Speed up the turtle for faster drawing
    turtle.speed(0)
    # Call the function with requested parameters for 8 petals
    draw_flower(a=100, n=4, end=6.28)
    
def draw_flower(a, n, end):
    #specify the colors to be used for drawing
    colors = ['#fce345', '#f6c455', '#fababc', '#b5dcda', '#a2cd54' ]
    #specify thickness of the pen
    turtle.width(3)
    t=0
   #draw the petals
    turtle.begin_fill()
    while t<end:
        turtle.color(random.choice(colors))
        x=a*sin(t*n)*cos(t)
        y=a*sin(t*n)*sin(t)
        turtle.goto(x,y)
        t=t+0.02
    turtle.end_fill()
    #draw three circles for the middle of the flower
    turtle.color(random.choice(colors))
    for i in range(3):
        turtle.circle(5+5*i)
        turtle.up()
        turtle.setpos(0,-(5+5*i))
        turtle.down()

if __name__ == "__main__":
    main()
