# We import our Shapes class from the
#   shapes.py modeule
from shapes import Shapes

def main():
    # Create an instance of the Shape class
    my_shape = Shapes()

    # Call methods on our shape instance
    my_shape.draw_rectangle(0, 0, 100, 50)
    my_shape.draw_equ_triangle(10, 50, 125)
    my_shape.draw_sprial(0, 0, 10, 50)

    # Keep the window open
    my_shape.wait()

if __name__ == "__main__":
    main()