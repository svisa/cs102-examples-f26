# without functions
# Explorer and Zombie walking game

import sys
import pygame

# --------------------------------------------------
# Set up Pygame
# --------------------------------------------------

pygame.init()

WIDTH = 640
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explorer and Zombie")

clock = pygame.time.Clock()


# --------------------------------------------------
# Load the images
# --------------------------------------------------

background = pygame.image.load("images/bgforest_small.png")

idle_image = pygame.image.load("images/idle.png")

explorer_images = [
    pygame.image.load("images/walk037.png"),
    pygame.image.load("images/walk038.png"),
    pygame.image.load("images/walk039.png"),
    pygame.image.load("images/walk040.png"),
    pygame.image.load("images/walk041.png"),
    pygame.image.load("images/walk042.png"),
    pygame.image.load("images/walk043.png")
]

zombie_images = [
    pygame.image.load("images/zwalk037.png"),
    pygame.image.load("images/zwalk038.png"),
    pygame.image.load("images/zwalk039.png"),
    pygame.image.load("images/zwalk040.png"),
    pygame.image.load("images/zwalk041.png"),
    pygame.image.load("images/zwalk042.png"),
    pygame.image.load("images/zwalk043.png")
]

emote_images = [
    pygame.image.load("images/emote_dots1.png"),
    pygame.image.load("images/emote_dots2.png"),
    pygame.image.load("images/emote_dots3.png")
]

exclamation_image = pygame.image.load(
    "images/emote_exclamation.png"
)


# --------------------------------------------------
# Set up the explorer
# --------------------------------------------------

explorer_x = -50
explorer_y = 400

explorer_image = idle_image

explorer_frame = 0
explorer_timer = 0


# --------------------------------------------------
# Set up the zombie
# --------------------------------------------------

zombie_x = -50
zombie_y = 400

zombie_image = zombie_images[0]

zombie_frame = 0
zombie_timer = 0


# --------------------------------------------------
# Set up the emote
# --------------------------------------------------

emote_image = emote_images[0]

emote_frame = 0
emote_timer = 0

emote_x = 0
emote_y = 0


# --------------------------------------------------
# The animation has three states
#
# State 0: Explorer walks toward the middle
# State 1: Zombie approaches explorer
# State 2: Explorer and zombie run away
# --------------------------------------------------

current_state = 0


# --------------------------------------------------
# The main game loop
# --------------------------------------------------

running = True

while running:

    # --------------------------------------------------
    # Find out how much time has passed
    # --------------------------------------------------

    milliseconds = clock.tick(60)

    # Convert milliseconds to seconds
    dt = milliseconds / 1000


    # --------------------------------------------------
    # Check for events
    # --------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # --------------------------------------------------
    # Update the animation
    # --------------------------------------------------

    # ================================================
    # STATE 0
    # Explorer walks toward the middle
    # ================================================

    if current_state == 0:

        # Move the explorer to the right
        explorer_x += 20 * dt

        # Animate the explorer
        explorer_timer += dt

        if explorer_timer >= 0.2:

            explorer_timer = 0

            explorer_frame += 1

            explorer_image = explorer_images[
                explorer_frame % len(explorer_images)
            ]

        # Has the explorer reached the middle?
        if explorer_x > WIDTH // 2:

            # Stop the explorer's walking animation
            explorer_image = idle_image

            # Move to the next state
            current_state = 1


    # ================================================
    # STATE 1
    # Zombie approaches the explorer
    # ================================================

    elif current_state == 1:

        # Move the zombie toward the explorer
        if zombie_x < explorer_x - 150:

            zombie_x += 20 * dt

        else:

            # Zombie is close enough.
            # Start the final state.

            current_state = 2


        # --------------------------------------------
        # Animate the zombie
        # --------------------------------------------

        zombie_timer += dt

        if zombie_timer >= 0.2:

            zombie_timer = 0

            zombie_frame += 1

            zombie_image = zombie_images[
                zombie_frame % len(zombie_images)
            ]


        # --------------------------------------------
        # Animate the emote
        # --------------------------------------------

        emote_timer += dt

        if emote_timer >= 0.5:

            emote_timer = 0

            emote_frame += 1


        # Put the emote above the explorer
        emote_x = explorer_x
        emote_y = explorer_y - 50

        # Change from "..." to "!" when the zombie
        # gets close
        if zombie_x < explorer_x // 2:

            emote_image = emote_images[
                emote_frame % len(emote_images)
            ]

        else:

            emote_image = exclamation_image


    # ================================================
    # STATE 2
    # Explorer and zombie run away
    # ================================================

    elif current_state == 2:

        # Move both characters to the right
        explorer_x += 20 * dt
        zombie_x += 20 * dt


        # --------------------------------------------
        # Continue animating the explorer
        # --------------------------------------------

        explorer_timer += dt

        if explorer_timer >= 0.2:

            explorer_timer = 0

            explorer_frame += 1

            explorer_image = explorer_images[
                explorer_frame % len(explorer_images)
            ]


        # --------------------------------------------
        # Continue animating the zombie
        # --------------------------------------------

        zombie_timer += dt

        if zombie_timer >= 0.2:

            zombie_timer = 0

            zombie_frame += 1

            zombie_image = zombie_images[
                zombie_frame % len(zombie_images)
            ]


    # --------------------------------------------------
    # Draw everything
    # --------------------------------------------------

    # Draw the background first
    screen.blit(background, (0, 0))


    # Draw the explorer
    screen.blit(
        explorer_image,
        (explorer_x, explorer_y)
    )


    # Draw the emote and zombie during state 1
    if current_state == 1:

        screen.blit(
            emote_image,
            (emote_x, emote_y)
        )

        screen.blit(
            zombie_image,
            (zombie_x, zombie_y)
        )


    # Draw the zombie during state 2
    elif current_state == 2:

        screen.blit(
            zombie_image,
            (zombie_x, zombie_y)
        )


    # Show everything we just drew
    pygame.display.flip()


# --------------------------------------------------
# Quit Pygame
# --------------------------------------------------

pygame.quit()
sys.exit()