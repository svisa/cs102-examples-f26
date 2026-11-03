import turtle

# Move the turtle to the angle of the circle
#	where you'd like to begin the drawing
turtle.penup()
turtle.circle(100, 90)

# Start drawing the "rest" of your circle/arc
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(100, 180)
turtle.end_fill()

