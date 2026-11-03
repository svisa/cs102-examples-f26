from PIL import Image
from pathlib import Path


def avg_luminance(color):
    r, g, b = color
    return (r + g + b) / 3


# To embed the image, we consider a secret image to be
#	black and white, and the destination image to be
#	any image with a size >= the secret image.
def embed_secret_message(secret_path, dest_path):
    secret_image = Image.open(secret_path)
    destination_image = Image.open(dest_path)

    secret_pixels = secret_image.load()
    destination_pixels = destination_image.load()

    width, height = destination_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = destination_pixels[x,y]
            
            # Make the red channel and even number
            if r % 2 != 0:
                if r == 255:
                    r -= 1
                else:
                    r += 1
            
            destination_pixels[x,y] = (r, g, b)
            
            if x >= secret_image.size[0] or y >= secret_image.size[1]:
                continue
            
            # If our secret image has a relatively dim pixel (like black)
            #	make the red channel an odd number.
            if avg_luminance(secret_pixels[x, y]) < 100:
                destination_pixels[x,y] = (r + 1, g, b)

    return destination_image


# Decode or extract the secret image from an existing image
def reveal_secret_message(image_path):
    picture = Image.open(image_path)
    pixels = picture.load()
    width, height = picture.size
    
    # Create a new image to store the extracted secret image
    secret = Image.new('RGB', (width, height), (255, 255, 255))
    secret_pixels = secret.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
             
            # Look for odd red channel values and set that color to be black.
            if r % 2 != 0:
                secret_pixels[x, y] = (0, 0, 0)

    return secret
    

secret = Path('images/steganography/never.png')
destination = Path('images/steganography/board_game_pieces.jpg')

embed_secret_message(secret, destination).save('stego.png', 'PNG')
reveal_secret_message(Path('stego.png')).show()
                
            

