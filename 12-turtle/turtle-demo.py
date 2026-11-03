# Turtle is a drawing tool where to provide commands to a
#	representation of a physical object (the turtle) and
#	as the object repositions itself, it can draw lines
#	and shapes with a variety of colors.
#	You can find the official documentation and tutorial for turtle
#	here: https://docs.python.org/3.10/library/turtle.html

# First we need to import the turtle module for use
import turtle

# Drawing in Turtle doesn't happen in the terminal window
#	like when we use print(). Instead the Turtle draws on
#	a new screen (a new window).

screen = turtle.getscreen()

# By default, the "turtle" is a black arrow in the middle of the
#	Window. If you'd like it to look more "turtle-like, you can
#	change the image to an actual turtle.
turtle.shape("turtle")

# When using turtle, it starts at its "home" at the center of the window
#	or (0,0) in x/y coordinates facing right. When you request the Turtle
#	to move, it trails a line behind it to draw.

# This tells the turtle to move in the direction it is "facing" 100 units
turtle.forward(100)

# We can ask the turtle to rotate itself left or right some number of degrees
turtle.left(90)

# When we tell it to move forward again, it now moves "up" 100 units
turtle.forward(100)

# Using just what we know so far, can you draw a square? Can you draw the
#	square using a loop? Can you make a function that takes the width,
#	height, and a turtle as parameters to draw a square or rectangle using
#	the turtle?

# Let's clear the screen and send the turtle back home (to the center of
#	the screen) and facing right.
turtle.clear()
turtle.home()

# Huh...it still is drawing on the screen...I didn't want that...
#	Well the turtle carries a little pen with it wherever it goes
#	if you don't want to draw, you have to tell the turtle to lift
#	the pen up
turtle.penup()
turtle.clear()
turtle.home()

turtle.forward(100)

# Oops, forgot to tell the turtle to lower the pen...
turtle.pendown()
turtle.backward(100)
# much better

# We can also tell the turtle to travel to an arbitrary position on
#	the screen. Let's move home, clear the screen and jump to each
#	quadrant jump to each of the screen.
turtle.home()
turtle.clear()
turtle.goto(-100, 100) # Upper left
turtle.goto(100, 100)  # Upper right
turtle.goto(-100, -100)# Lower left
turtle.goto(100, -100) # Lower right

# Take note how using goto() draws a straight line from the turtle's
#	last location to the new location

# While the black ink is effective, we want a little more color on the
#	screen
turtle.color('blue')
# Notice how the turtle changed color...
turtle.home()
# Now anytime the turtle has the pen down it will draw in the color of
#	its body.

# Turtle can support many colors by name alone. The following list is not
#	complete, but here are some examples: yellow, gold, orange, red,
#	maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise,
#	lightgreen, green, darkgreen, chocolate, brown, black, gray, white.

# Additionally, turtle allows you to manually set the color using precise
#	color codes...like hot pink!
turtle.color('#FF69B4') 
turtle.right(180)
turtle.forward(150)

# Does that color string look familiar? It should...
#	You can represent colors using six hexidecimal values. Why six?
#	Each pair of hexideciaml numbers represent one byte or 8 bits.
#	Each byte of data represents the amount of red, green, and blue
#	color used respectively. Since we have one byte for each color,
#	the values can only be between 0 and 255. Let's see if we can
#	make it red using only hexideciaml
turtle.color('#FF0000')
# Nice! FF is 255 for the first hex pair which makes the turtle pure red.
#	Try to change the code to make it just blue, and then just green.

# Hex codes can be hard to remember, so we can also supply the values
#	for red, green, and blue. The default behavoir is to represent the
#	color triplet as percentages(values 0-1).
turtle.color(0.8, 0, .96) # Hot Purple: 80% red, 0% green, 96% blue
# We can change the color mode to 255 so we can represent them as values
#	which is more similar to the hexidecimal representation.
turtle.colormode(255)
turtle.color(203, 0, 245) # Hot Purple: 203 red, 0 green, 245 blue

# RGB is an additive color model. In that the three colors are the blending
#	of three separate light sources (the tiny lights that make up the screen
#	of your computer). These separate light sources (red, green, and blue)
#	are called sub-pixels, and then combination of the intensity at which
#	each of the three glow creates one pixel. Cool huh? :)
#	There are different models to represent color, and some have specific use
#	cases to most accurately display color on the medium on which they
#	appear. Check out the article:
#	https://pavilion.dinfos.edu/Article/Article/2355687/additive-subtractive-color-models/


# While you can draw your own shapes using turtle, some are built in for you
turtle.clear()
turtle.color("purple")
turtle.penup()
turtle.home()

turtle.goto(-200, -200)
turtle.pendown()

# Draw a circle with a radius of 50.
turtle.circle(50)
turtle.penup()
turtle.sety(-150)
# Draw a gold dot with a size of 10.
turtle.dot(10, 'gold')

turtle.penup()
turtle.home()

# This prevents the window with your lovely work of art from being
#	closed until you exit the turtle window.
turtle.mainloop()
