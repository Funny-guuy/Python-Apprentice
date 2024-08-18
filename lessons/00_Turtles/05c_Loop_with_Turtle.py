
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
sides = int(input())
angle = (360 / sides)
tina = turtle.Turtle()                  # Create a turtle named tina
for i in range(sides):
    tina.forward(150)
    tina.left(angle)

turtle.exitonclick()                    # Close the window when we click on it
