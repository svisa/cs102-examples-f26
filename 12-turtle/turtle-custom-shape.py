import turtle

# Set a custom shape from file
#	Note that using an image does not support
#	rotating the image like the standard turtle does
turtle.register_shape('pumpkin.gif')
turtle.shape('pumpkin.gif')
turtle.circle(100, 90)

# Start drawing the "rest" of your circle/arc
turtle.pendown()
turtle.circle(100, 180)

# You can "stamp" the turtle's current shape
#	onto the screen
turtle.penup()
turtle.home()
turtle.pendown()
turtle.stamp()

# You can also build a custom shape by supplying points.
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

# The coordinate points are not with respect to
#	the turtles current position, but instead the
#	home position (0,0).
coordinates = ( (-5, 0), (0, 5), (5, 0), (0, -5) )

turtle.register_shape('diamond', coordinates)
turtle.shape('diamond')
turtle.stamp()
turtle.forward(100)

# shapes can be deformed by using shapesize
#	You can provide values to stretch the width
#	and length respectively.
turtle.shapesize(10, 3)

