import turtle
import pygame

turtle.Screen().bgcolor("dark slate blue")

# Start the music
pygame.mixer.init()
pygame.mixer.music.load("relaxing-guitar.mp3")
pygame.mixer.music.play(-1)       # -1 means repeat forever
# https://pixabay.com/ has free music and images

t = turtle.Turtle()
t.speed(0)

def drawSquare(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def drawFlower():
    for i in range(36):
        drawSquare(100)
        t.right(10)

drawFlower()

#turtle.done()

t.goto(220,220)
t.pencolor("red")
t.fillcolor("yellow")

def drawCircle(size):
    t.circle(size)

def drawFlower():
    for i in range(36):
        drawCircle(50)
        t.right(10)
        
t.begin_fill()
drawFlower()
t.end_fill()


def draw_spiral(x, y, initial_radius, arc_count, line_color="Yellow"):
    t.goto(x, y)
    #t.turtle.color(line_color)
    for i in range(arc_count):
        # The 45 determines what portion of the circle to draw..this draws a 45 degree arc
        t.circle(initial_radius + i, 45)
        
draw_spiral(-150, 200, 10, 50)

turtle.done()

# Stop the music when the program ends
pygame.mixer.music.stop()
pygame.quit()