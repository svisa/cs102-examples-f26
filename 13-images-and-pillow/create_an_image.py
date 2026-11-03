# You can find all sorts of different methods that can be
#	used to draw on an image with the Pillow documentation
#	https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
#	DO NOT MEMORIZE THE DOCUMENTATION :)
from PIL import Image, ImageDraw

# Create a new image that supports transparency
#	Using RGBA (red, greenm blue, alpha).
#	Alpha is the transparency value ranging from
#	transparent (0) to opaque (255).
img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))

# We can draw on an image as well!
draw = ImageDraw.Draw(img)

# The ellipse is defined in an interesting way. The first two
#	value are an upper-left point and the last two are a bottom-left
#	point. These two points are use to form a bounding box, and the
#	circle is simply drawn within that box. The fill is the color
#	to make the circle (in this case, red).
draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

# We save the result as a GIF since that format support transparency
#	but a PNG would work as well.
img.save('test.gif', 'GIF', transparent=0)

