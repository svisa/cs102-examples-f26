from PIL import Image
from pathlib import Path


def crop(image, tlx, tly, brx, bry):
    cropped_picture = Image.new('RGB', (brx-tlx, bry-tly), (255, 255, 255))
    dest_pixels = cropped_picture.load()
    source_pixels = image.load()
    
    dest_x = 0
    for source_x in range(tlx, brx):
        dest_y = 0
        
        for source_y in range(tly, bry):
            color = source_pixels[source_x, source_y]
            dest_pixels[dest_x, dest_y] = color
            dest_y += 1
        
        dest_x += 1
    
    return cropped_picture
            

def rotate(image, degree):
    
    if degree % 360 == 0:
        return image.copy()
        
    width, height = image.size
    source_pixels = image.load()

    rotated_picture = None
    if degree % 180 == 0:
        rotated_picture = Image.new('RGB', (width, height))
    else:
        rotated_picture = Image.new('RGB', (height, width))
    
    rotated_pixels = rotated_picture.load()
    
    if degree % 360 == 90:
        r_x = 0
        for y in range(height-1, -1, -1):
            r_y = 0
            for x in range(width):
                rotated_pixels[r_x, r_y] = source_pixels[x, y]
                r_y += 1
            r_x += 1
    elif degree % 360 == 180:
        r_y = 0
        for y in range(height - 1, -1 , -1):
            r_x = 0
            for x in range(width - 1, -1, -1):
                rotated_pixels[r_x, r_y] = source_pixels[x, y]
                r_x += 1
            r_y += 1
    elif degree % 360 == 270:
        r_y = 0
        for x in range(width-1, -1, -1):
            r_x = 0
            for y in range(height):
                rotated_pixels[r_x, r_y] = source_pixels[x, y]
                r_x += 1
            r_y += 1
    return rotated_picture


pic = Image.open(Path('images/alphabet.jpg'))
cropped_image = crop(pic, 67, 116, 206, 251)
cropped_image.show()

pic = Image.open(Path('images/alphabet.jpg'))
rotated_image = rotate(pic, 90)
rotated_image.show()

pic = Image.open(Path('images/alphabet.jpg'))
rotated_image = rotate(pic, 180)
rotated_image.show()

pic = Image.open(Path('images/alphabet.jpg'))
rotated_image = rotate(pic, 270)
rotated_image.show()


