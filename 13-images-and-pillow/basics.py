# Import the Image class from the Pillow (PIL) module
from PIL import Image
from pathlib import Path

import math

# A function for approximating how similar two colors are
def color_difference(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    
    # This is a euclidean distance over all three values
    #	of the color (r, g, b).
    return math.sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)

# Open an image file from your computer
# Using Path here to support macOS or Windows file paths
pic = Image.open(Path('images/alphabet.jpg'))

# You can find out details about the image such as:
print(f"Format: {pic.format}")
print(f"Image Size: {pic.size}")
print(f"Mode: {pic.mode}")

# Disply an image
pic.show()

# Let's create a copy for the image (in memory)
#	so we don't change the original
pic2 = pic.copy()

# Get the pixel data for the image. This can
#	be slow, so be patient.
pixels = pic2.load()

# We can now access each individual pixel as a grid
#	of (x, y) coordinates where (0, 0) is the top-left
#	pixel of an image. Since pixels is an object created
#	by the load() method, the creators of Pillow provided
#	a fancy way to access the x,y corrdinates using a pair
#	of values for the index.

print(pixels[0, 0]) # Get the top left pixel at the x,y coordinate (0, 0)

# Let's change all the red letters to be pink!
pink = (255, 20, 147)
image_width, image_height = pic2.size
for x in range(image_width):
    for y in range(image_height):
        r, g, b = pixels[x, y]
        
        # While we can compare each color channel to find a color
        #	we wish to replace Like this:
        #	if 245 <= r <= 255 and g < 100 and b < 100
    
        # It may be more convenient to simply determine how
        #	different two colors are...that is, the distance
        #	between them. We can use a euclidean distance
        #	(like with points on a graph) to approximate this.
        red = (255, 0, 0)
        if color_difference(red, pixels[x, y]) < 75:
            pixels[x, y] = pink

# Display the new image
pic2.show()

# Save the new image to a file
pic2.save('pink_alphabet.jpg')

# Manipulate Pixels in a specific area of the picture
black = (0, 0, 0)
for x in range(351, 469):
    for y in range(114, 252):
        if color_difference(black, pixels[x, y]) > 100:
            pixels[x, y] = (0, 255, 0)
            
pic2.show()
        