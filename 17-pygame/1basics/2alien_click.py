
import sys
import pygame


# --------------------------------------------------
# Set up Pygame
# --------------------------------------------------

pygame.init()

WIDTH = 600

# Load the alien image so we can determine its height
alien_normal = pygame.image.load("images/alien.png")
alien_hurt = pygame.image.load("images/alien_hurt.png")

HEIGHT = alien_normal.get_height() + 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Game")

clock = pygame.time.Clock()


# --------------------------------------------------
# Set up the alien
# --------------------------------------------------

# The alien starts just off the top-right corner
alien_x = WIDTH
alien_y = 10

# Start with the normal alien picture
alien_image = alien_normal

# Keep track of the score
score = 0


# --------------------------------------------------
# Set up the sound
# --------------------------------------------------

eep_sound = pygame.mixer.Sound("sounds/eep.wav")


# --------------------------------------------------
# Timer for changing the alien back to normal
# --------------------------------------------------

hurt_timer = 0


# --------------------------------------------------
# Main game loop
# --------------------------------------------------

running = True

while running:

    # Find out how much time has passed
    milliseconds = clock.tick(60)

    # Convert milliseconds to seconds
    dt = milliseconds / 1000


    # --------------------------------------------------
    # Check for events
    # --------------------------------------------------

    for event in pygame.event.get():

        # Did the player close the window?
        if event.type == pygame.QUIT:
            running = False


        # Did the player click the mouse?
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Get the location of the mouse click
            mouse_x, mouse_y = event.pos

            # Create a rectangle around the alien
            alien_rect = alien_image.get_rect(
                topleft=(alien_x, alien_y)
            )

            # Check whether the mouse clicked the alien
            if alien_rect.collidepoint(mouse_x, mouse_y):

                # The player hit the alien
                alien_image = alien_hurt

                # Increase the score
                score += 1

                # Play the sound
                eep_sound.play()

                # Start the hurt timer
                hurt_timer = 0.75

            else:

                # The player missed the alien
                score -= 1


    # --------------------------------------------------
    # Update the alien
    # --------------------------------------------------

    # Move the alien to the right
    alien_x += 2


    # If the alien has moved completely off the
    # right side of the screen, start it again
    # on the left side.
    if alien_x > WIDTH:

        alien_x = 0


    # --------------------------------------------------
    # Update the hurt timer
    # --------------------------------------------------

    if hurt_timer > 0:

        # Count down the timer
        hurt_timer -= dt

        # Has 0.75 seconds passed?
        if hurt_timer <= 0:

            # Change the alien back to normal
            alien_image = alien_normal


    # --------------------------------------------------
    # Draw everything
    # --------------------------------------------------

    # Clear the screen
    screen.fill((0, 0, 0))


    # Draw the alien
    screen.blit(
        alien_image,
        (alien_x, alien_y)
    )


    # Create the font used for the score
    font = pygame.font.Font(None, 30)

    # Create the score text
    score_text = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )

    # Find the rectangle surrounding the text
    score_rect = score_text.get_rect()

    # Position the bottom-right corner
    score_rect.bottomright = (WIDTH - 10, HEIGHT - 5)

    # Draw the score
    screen.blit(score_text, score_rect)


    # Show everything on the screen
    pygame.display.flip()


# --------------------------------------------------
# Quit Pygame
# --------------------------------------------------

pygame.quit()
sys.exit() # to close the window


