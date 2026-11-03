# key pressed → set direction → move character → change animation frames
#      → key released → return to idle.
# use L and R arrows to make person walk

import sys
import pygame

# -------------------------
# Window properties
# -------------------------
WIDTH = 600
HEIGHT = 200

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Walking Animation Example")

clock = pygame.time.Clock()

# -------------------------
# Explorer setup
# -------------------------
def setup_explorer():

    global explorer
    global idle_image
    global walk_left_images
    global walk_right_images
    global explorer_x
    global explorer_y

    # Load the idle image
    idle_image = pygame.image.load(
        "images/e_idle.png"
    ).convert_alpha()

    # Load the walking images
    walk_left_images = []
    walk_right_images = []

    for number in range(1, 8):

        left_image = pygame.image.load(
            f"images/e_walkleft{number}.png"
        ).convert_alpha()

        right_image = pygame.image.load(
            f"images/e_walkright{number}.png"
        ).convert_alpha()

        walk_left_images.append(left_image) #list of seven images moving left
        walk_right_images.append(right_image)

    # Position the explorer in the middle
    # of the screen at the bottom.

    explorer_x = WIDTH // 2

    # The y coordinate represents the top
    # of the image, so subtract the image height.
    explorer_y = HEIGHT - idle_image.get_height()

# -------------------------
# Animation variables
# -------------------------
explorer_x = 0
explorer_y = 0

idle_image = None
walk_left_images = []
walk_right_images = []

# Current direction:
# None, "left", or "right"
walk_direction = None

# Current animation frame
walk_frame = 0

# Time since the last animation frame
animation_timer = 0

# How often the animation changes frames
ANIMATION_SPEED = 0.09

# -------------------------
# Draw everything
# -------------------------
def draw():

    screen.fill((255, 255, 255))

    # Choose the correct image
    if walk_direction == "left":

        image = walk_left_images[walk_frame]

    elif walk_direction == "right":

        image = walk_right_images[walk_frame]

    else:

        image = idle_image

    screen.blit(
        image,
        (explorer_x, explorer_y)
    )

# -------------------------
# Move the explorer
# dt represents the amount of time that has passed since the previous frame
# -------------------------
def move_explorer(dt):

    global explorer_x

    if walk_direction == "right":

        explorer_x += 200 * dt

    elif walk_direction == "left":

        explorer_x -= 200 * dt

# -------------------------
# Animate the explorer
# dt represents the amount of time that has passed since the previous frame
# -------------------------
def animate_explorer(dt):

    global walk_frame
    global animation_timer

    # Only animate while walking
    if walk_direction is None:

        return

    # Add the time since the last frame
    animation_timer += dt

    # Change the image every 0.09 seconds
    if animation_timer >= ANIMATION_SPEED:

        walk_frame += 1

        # Start again at frame 0
        # after the last frame.
        if walk_frame >= 7:
            walk_frame = 0

        animation_timer = 0

# -------------------------
# Handle keyboard events
# -------------------------
def handle_events():

    global walk_direction
    global walk_frame
    global animation_timer

    for event in pygame.event.get():

        # Close the window
        if event.type == pygame.QUIT:

            return False

        # A key was pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                return False

            # Start walking right
            if event.key == pygame.K_RIGHT:

                walk_direction = "right"
                walk_frame = 0
                animation_timer = 0

            # Start walking left
            elif event.key == pygame.K_LEFT:

                walk_direction = "left"
                walk_frame = 0
                animation_timer = 0


        # A key was released
        if event.type == pygame.KEYUP:

            if (
                event.key == pygame.K_RIGHT
                or event.key == pygame.K_LEFT
            ):

                # Return to the idle image
                walk_direction = None
                walk_frame = 0
                animation_timer = 0

    return True

# -------------------------
# Main game loop
# -------------------------
def main():

    setup_explorer()

    running = True

    while running:

        # Time since the previous frame
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000

        # Handle keyboard and window events
        running = handle_events()

        # Move the character
        move_explorer(dt)

        # Change animation frames
        animate_explorer(dt)

        # Draw everything
        draw()

        pygame.display.flip()

    pygame.quit()

# -------------------------
# Start the game
# -------------------------

main()
sys.exit()



