import turtle

# You can setup the turtle to have a specific
# size of your drawing "canvas"
turtle.setup(width=1000, height=1000)

# You can also set the color of the background
# You can set your own specific colors, or use
# the list of predefined colors...there's lots.
# https://cs111.wellesley.edu/labs/lab02/colors
turtle.bgcolor("Beige")

# Sets the line color and fill color
turtle.color("black", "blue")

# Start a fill
turtle.begin_fill()

# Draw a closed shape
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

# End the color fill
turtle.end_fill()

# Prevents turtle from drawing while
# it moves
turtle.penup()

# (0,0) is the center or home
# for the turtle
turtle.home()

turtle.goto(-200, 200) # Upper left

# Put the pen down to begin drawing again.
turtle.pendown()

# Sets the line color
turtle.color("Purple")

# Rotate the turtle to point
# in a fixed cardinal direction.
# North (up) = 90
# South (down) = 270
# East (right) = 0
# West (left) = 180
turtle.setheading(270)
turtle.forward(100)

turtle.penup()
turtle.color("Pink", "Pink")
turtle.goto(250, -250)
turtle.setheading(0)
turtle.pendown()
turtle.begin_fill()
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

# Lot of work...maybe we should...
# use one of our tools to create
# a shape like the square above...
# hmmmm

# Make the turtle not show
turtle.hideturtle()
turtle.mainloop()

