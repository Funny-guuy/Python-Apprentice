"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""
sides = input()
# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
angle = (360 / int(sides))
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(int(sides))
# Use tina.forward() and tina.left() to draw a triangle
for i in range(int(sides)):
    tina.forward(90)
    tina.left(angle)
# Make each side of the triangle a different color with 
# tina.pencolor()
    tina.pencolor("green")
... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
