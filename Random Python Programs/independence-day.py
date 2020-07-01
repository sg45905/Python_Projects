'''
@author - Sarthak Gupta
'''

import turtle
import time

# create a screen
screen = turtle.getscreen()

# set background color of screen
screen.bgcolor("#b3daff")

# set title of screen
screen.title("Indian Flag")
stitle = turtle.Turtle()

# set the cursor/turtle speed. Higher value, faster is the turtle
stitle.speed(100)
stitle.penup()

# decide the shape of cursor/turtle
stitle.shape("turtle")

# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height/3
stripe_width = flag_width

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height / 2

def draw_fill_rectangle(x, y, height, width, color):
    stitle.goto(x,y)
    stitle.pendown()
    stitle.color(color)
    stitle.begin_fill()
    stitle.forward(width)
    stitle.right(90)
    stitle.forward(height)
    stitle.right(90)
    stitle.forward(width)
    stitle.right(90)
    stitle.forward(height)
    stitle.right(90)
    stitle.end_fill()
    stitle.penup()

# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    
    # we need to draw total 3 stripes, 1 saffron, 1 white and 1 green
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    
    # decrease value of y by stripe_height
    y = y - stripe_height   
    
    # create middle white stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    # create last green stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height

def draw_chakra():
    stitle.speed(1)
    stitle.goto(0,0)
    
    color = "#000080" # navy blue
    
    stitle.penup()
    stitle.color(color)
    stitle.fillcolor(color)
    stitle.goto(0, 0 - chakra_radius)
    stitle.pendown()
    stitle.circle(chakra_radius)
    
    # draw 24 spikes in chakra
    for _ in range(24):
        stitle.penup()
        stitle.goto(0,0)
        stitle.left(15)
        stitle.pendown()
        stitle.forward(chakra_radius)

# start after 5 seconds.
time.sleep(0)

# draw 3 stripes
draw_stripes()

# draw squares to hold stars
draw_chakra()

# hide the cursor/turtle
stitle.hideturtle()

# keep holding the screen until closed manually
screen.mainloop()
