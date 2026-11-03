# import Modules
from turtle import Turtle
from random import random

# Declare a class named Shapes
class Shapes:

    # Constructor to setup our shape drawing class
    def __init__(self, screen_width=800, screen_height=600, background="White"):
        self.turtle = Turtle()
        self.screen = self.turtle.screen
        self.screen.setup(screen_width, screen_height)
        self.screen.bgcolor(background)
        self.DIRECTIONS = {"N": 90, "S": 270, "W": 180, "E": 0}


    # Method to scribble randomly
    def scribble(self, x, y, number_of_scribbles, line_color="Black"):
        self.move_to(x, y)
        self.turtle.color(line_color)

        for _ in range(number_of_scribbles):
            steps = int(random() * 100) # Line lengths between 0 and 100
            angle = int(random() * 360) # Angles between 0 and 360
            self.turtle.right(angle)
            self.turtle.forward(steps)


    # Method to move the turtle and orient its direction
    def move_to(self, x, y, direction="E"):
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.setheading(self.DIRECTIONS[direction])
        self.turtle.pendown()


    # The underscore (_) indicates that this method is only
    #   intended for use within the class. This means we shouldn't
    #   call this method when using the class shape. In other programming
    #   languages, this would be considered a "private" method of the Shape class
    def _render_geometry(self, x, y, number_of_sides, side_length, line_color="Black", fill_color=None):
        self.move_to(x, y)
        self.turtle.color(line_color)

        if fill_color:
            self.turtle.fillcolor(fill_color)
            self.turtle.begin_fill()
        
        for _ in range(number_of_sides):
            self.turtle.fd(side_length)
            self.turtle.right(360 // number_of_sides)

        if fill_color:
            self.turtle.end_fill()

        # This function can also be achieved using the circle() method from Turtle


    # Method to draw a rectangle
    def draw_rectangle(self, x, y, length, width, line_color="Black", fill_color=None):
        self.move_to(x, y)
        
        if fill_color:
            self.turtle.fillcolor(fill_color)
            self.turtle.begin_fill()
        
        self.turtle.color(line_color)

        for side in range(4):
            if side % 2 == 0:
                self.turtle.forward(length)
                self.turtle.right(90)
            else:
                self.turtle.forward(width)
                self.turtle.right(90)

        if fill_color:
            self.turtle.end_fill()


    # Use our "private" helper method to create an equilateral triangle
    def draw_equ_triangle(self, x, y, side_length, line_color="Black", fill_color=None):
        self._render_geometry(x, y, 3, side_length, line_color, fill_color)


    # Method to draw a cool spiral
    def draw_sprial(self, x, y, initial_radius, arc_count, line_color="Black"):
        self.move_to(x, y)
        self.turtle.color(line_color)

        for i in range(arc_count):
            # The 45 determines what portion of the circle to draw..this draws a 45 degree arc
            self.turtle.circle(initial_radius + i, 45) 


    # This will be called to prevent the window from closing early.
    #   This doesn't appear to be necessary when using Thonny, but is
    #   for other programs.
    def wait(self):
        self.turtle.screen.mainloop()
