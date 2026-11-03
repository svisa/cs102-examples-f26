# this version uses functions to illustrate a game consisting of 
# events → update → draw → repeat
#
import sys
import pygame

# --------------------------------------------------
# Set up the game
# --------------------------------------------------

pygame.init()

WIDTH = 600

# Load the alien images
alien_normal = pygame.image.load("images/alien.png")
alien_hurt = pygame.image.load("images/alien_hurt.png")

# The height of the window is based on the alien's height
HEIGHT = alien_normal.get_height() + 40

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Game")

# Create a clock to control the speed of the game
clock = pygame.time.Clock()

# Load the sound
eep_sound = pygame.mixer.Sound("sounds/eep.wav")

# Create the font for the score
font = pygame.font.Font(None, 30)

# --------------------------------------------------
# Alien variables
# --------------------------------------------------

# location of alien
alien_x = WIDTH
alien_y = 10

# The alien starts with the normal image
alien_image = alien_normal

# The player's score
score = 0

# Timer used when the alien is hurt
hurt_timer = 0

# --------------------------------------------------
# Draw everything on the screen
# --------------------------------------------------

def draw():
    # Clear the screen by filling it with black
    screen.fill((0, 0, 0))

    # Draw the alien
    screen.blit(
        alien_image,
        (alien_x, alien_y)
    )

    # Create the score text
    score_text = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )

    # Position the score in the bottom-right corner
    score_rect = score_text.get_rect()
    score_rect.bottomright = (WIDTH - 10, HEIGHT - 5)

    # Draw the score
    screen.blit(score_text, score_rect)

    # Show everything we have drawn
    pygame.display.flip()


# --------------------------------------------------
# Handle mouse clicks and other events
# --------------------------------------------------

def handle_events():
    global score

    for event in pygame.event.get():

        # The player closed the window
        if event.type == pygame.QUIT:
            return False

        # The player clicked the mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Get the location of the mouse
            mouse_x, mouse_y = event.pos

            # Create a rectangle around the alien
            alien_rect = alien_image.get_rect(
                topleft=(alien_x, alien_y)
            )

            # Did the player click the alien?
            if alien_rect.collidepoint(mouse_x, mouse_y):

                # The player hit the alien
                set_alien_hurt()

                # Increase the score
                score += 1

            else:

                # The player missed
                score -= 1

    return True


# --------------------------------------------------
# Make the alien hurt
# --------------------------------------------------

def set_alien_hurt():
    global alien_image
    global hurt_timer

    # Change the alien's image
    alien_image = alien_hurt

    # Play the sound
    eep_sound.play()

    # Keep the hurt image for 0.75 seconds
    hurt_timer = 0.75


# --------------------------------------------------
# Change the alien back to normal
# --------------------------------------------------

def set_alien_normal():
    global alien_image

    alien_image = alien_normal


# --------------------------------------------------
# Update the game
# --------------------------------------------------

def update(dt):
    global alien_x
    global hurt_timer

    # Move the alien to the right
    alien_x += 2

    # If the alien has moved completely off
    # the right side of the screen, start it again
    # on the left side.
    if alien_x > WIDTH:
        alien_x = 0

    # ----------------------------------------------
    # Update the hurt timer
    # ----------------------------------------------

    if hurt_timer > 0:

        # Subtract the time that has passed
        hurt_timer -= dt

        # Has the 0.75 seconds passed?
        if hurt_timer <= 0:
            set_alien_normal()


# --------------------------------------------------
# Main game loop
# --------------------------------------------------

running = True

while running:

    # Wait until 60 frames have passed per second
    # controls the game speed and makes game run
    # at same speed over any computer 
    milliseconds = clock.tick(60)

    # Convert milliseconds to seconds
    dt = milliseconds / 1000

    # Handle keyboard, mouse, and window events
    running = handle_events()

    # Update the game
    update(dt)

    # Draw the game
    draw()


# --------------------------------------------------
# Quit Pygame
# --------------------------------------------------

pygame.quit()
sys.exit() # to close the window

