
# Pygame must be installed before running this program.
import sys
import pygame


# --------------------------------------------------
# Set up Pygame
# --------------------------------------------------

pygame.init()

# Set the size of the game window
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Pygame Program")


# Create a clock to control the speed of the game
clock = pygame.time.Clock()


# --------------------------------------------------
# Main game loop
# --------------------------------------------------

running = True

while running:

    # --------------------------------------------------
    # Check for events
    # --------------------------------------------------

    for event in pygame.event.get():

        # Did the player close the window?
        if event.type == pygame.QUIT:
            running = False

        # Did the player press a key?
        elif event.type == pygame.KEYDOWN:

            # Was the Escape key pressed?
            if event.key == pygame.K_ESCAPE:
                running = False


    # --------------------------------------------------
    # Draw the screen
    # --------------------------------------------------

    # Fill the entire screen with red.
    #
    # The three numbers represent:
    #     Red, Green, Blue
    #
    # Each value can be between 0 and 255.
    #
    # (255, 0, 0) means:
    #     255 Red
    #       0 Green
    #       0 Blue
    screen.fill((255, 0, 0))


    # Show the new screen; flip updates the entire screen at once
    pygame.display.flip()


    # Run the game at a maximum of 60 frames per second
    clock.tick(60)


# --------------------------------------------------
# Quit Pygame
# --------------------------------------------------

pygame.quit()
sys.exit() # to close the window

