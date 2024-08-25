""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
... # Your Code Here
#set_turtle_image(t, "leaguebot_bolt.gif")
t.turtlesize(stretch_wid= 5, stretch_len=5, outline= 5)
t.pencolor("blue") 
sides = input()
sides = int(sides)
angle = (360 / sides)
angle = int(angle)               
for i in range(sides):
    t.forward(150)
    t.left(angle)
turtle.done()