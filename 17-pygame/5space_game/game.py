# space game: the rocket shoots laser at falling asteroids
# use arrows to move L and R
# use space to shoot out with laser

import sys
import pygame
import random

# -------------------------
# Window properties
# -------------------------

WIDTH = 800
HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE!!!")

clock = pygame.time.Clock()

# -------------------------
# Load images
# -------------------------

background_image = pygame.image.load(
    "images/background-purple.png"
).convert()

game_title_image = pygame.image.load(
    "images/game-title.png"
).convert_alpha()

press_enter_image = pygame.image.load(
    "images/press-enter.png"
).convert_alpha()

game_over_image = pygame.image.load(
    "images/game-over.png"
).convert_alpha()

player_image = pygame.image.load(
    "images/pixel_ship_blue.png"
).convert_alpha()

laser_image = pygame.image.load(
    "images/pixel_laser_blue.png"
).convert_alpha()

asteroid_image = pygame.image.load(
    "images/asteroid_grey.png"
).convert_alpha()

thruster_images = [
    pygame.image.load(
        "images/thruster-1.png"
    ).convert_alpha(),

    pygame.image.load(
        "images/thruster-2.png"
    ).convert_alpha(),

    pygame.image.load(
        "images/thruster-3.png"
    ).convert_alpha(),

    pygame.image.load(
        "images/thruster-4.png"
    ).convert_alpha()
]

# -------------------------
# Load sounds
# -------------------------
explode_sound = pygame.mixer.Sound("sounds/explode.wav")
laser_sound = pygame.mixer.Sound("sounds/laser.wav")

# -------------------------
# Game states
# -------------------------
TITLE = "title"
GAME = "game"
GAMEOVER = "gameover"

current_state = TITLE

# -------------------------
# Create the player
# -------------------------
player_rect = player_image.get_rect()

player_rect.center = (
    WIDTH // 2,
    HEIGHT - 100
)

# -------------------------
# Create the thruster
# -------------------------
thruster_frame = 0
thruster_direction = 1

thruster_rect = thruster_images[0].get_rect()

thruster_rect.midtop = player_rect.midbottom

# -------------------------
# Lists of lasers and asteroids
# -------------------------
lasers = []
asteroids = []

# -------------------------
# Timers
# -------------------------
asteroid_timer = 0
thruster_timer = 0

# -------------------------
# Draw the background
# -------------------------
def draw_background():

    # The background image is 400 x 400,
    # so draw it four times to fill the screen.

    for x in range(0, WIDTH, 400):
        for y in range(0, HEIGHT, 400):
            screen.blit(background_image, (x, y))

# -------------------------
# Draw the main menu
# -------------------------
def draw_main_menu():

    title_rect = game_title_image.get_rect(
        midtop=(400, 200)
    )

    screen.blit(game_title_image, title_rect)

    screen.blit(press_enter_image, (300, 500))

# -------------------------
# Draw the game-over screen
# -------------------------
def draw_game_over():

    screen.blit(game_over_image, (200, 200))
    screen.blit(press_enter_image, (300, 500))

# -------------------------
# Draw lasers
# -------------------------
def draw_lasers():

    for laser in lasers:
        screen.blit(laser_image, laser)

# -------------------------
# Draw asteroids
# -------------------------
def draw_asteroids():

    for asteroid in asteroids:
        screen.blit(asteroid_image, asteroid)

# -------------------------
# Draw everything
# -------------------------
def draw():

    # Draw the background first.
    draw_background()

    if current_state == TITLE:

        draw_main_menu()

    elif current_state == GAME:

        draw_lasers()

        screen.blit(
            thruster_images[thruster_frame],
            thruster_rect
        )

        screen.blit(player_image, player_rect)

        draw_asteroids()

    elif current_state == GAMEOVER:

        draw_game_over()

# -------------------------
# Check the left and right keys
# -------------------------
def check_keys(dt):

    if current_state == GAME:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            player_rect.x -= int(dt * 300)

            # Keep the player inside the screen
            if player_rect.left < 0:
                player_rect.left = 0

        if keys[pygame.K_RIGHT]:

            player_rect.x += int(dt * 300)

            # Keep the player inside the screen
            if player_rect.right > WIDTH:
                player_rect.right = WIDTH

# -------------------------
# Animate the thrusters
# -------------------------
def animate_thrusters():

    global thruster_frame
    global thruster_direction

    # Reverse direction when we reach
    # either end of the animation.

    if not (
        0 <= thruster_frame + thruster_direction
        < len(thruster_images)
    ):
        thruster_direction *= -1

    thruster_frame += thruster_direction

# -------------------------
# Move the thrusters
# -------------------------
def move_thrusters():

    thruster_rect.midtop = player_rect.midbottom

# -------------------------
# Move the lasers
# -------------------------
def move_lasers(dt):

    for laser in lasers:
        laser.y -= int(dt * 400)
# -------------------------
# Move the asteroids
# -------------------------
def move_asteroids(dt):

    for asteroid in asteroids:

        asteroid.y += int(dt * 400)

# -------------------------
# Check laser collisions
# -------------------------
def check_laser_collisions():

    global lasers
    global asteroids

    lasers_to_remove = []
    asteroids_to_remove = []

    for laser in lasers:

        for asteroid in asteroids:

            if laser.colliderect(asteroid):

                lasers_to_remove.append(laser)
                asteroids_to_remove.append(asteroid)

                explode_sound.play()

                # Stop checking this laser after
                # it hits an asteroid.
                break

    # Remove the lasers that hit asteroids
    for laser in lasers_to_remove:

        if laser in lasers:
            lasers.remove(laser)

    # Remove the asteroids that were hit
    for asteroid in asteroids_to_remove:

        if asteroid in asteroids:
            asteroids.remove(asteroid)

# -------------------------
# Check player collisions
# -------------------------
def check_player_collisions():

    global current_state
    global asteroids
    global lasers
    global asteroid_timer
    global thruster_timer
    global thruster_frame

    for asteroid in asteroids:

        if player_rect.colliderect(asteroid):

            # Game over
            current_state = GAMEOVER

            explode_sound.play()

            # Stop the timers
            asteroid_timer = 0
            thruster_timer = 0

            # Reset the thruster animation
            thruster_frame = 0

            # Remove all asteroids and lasers
            asteroids = []
            lasers = []

            break

# -------------------------
# Remove objects that
# have left the screen
# -------------------------
def clean_up():

    global lasers
    global asteroids

    new_lasers = []

    for laser in lasers:

        # Keep the laser if it is still
        # on the screen.

        if laser.bottom >= 0:
            new_lasers.append(laser)

    lasers = new_lasers

    new_asteroids = []

    for asteroid in asteroids:

        # Keep the asteroid if it is still
        # on the screen.

        if asteroid.top <= HEIGHT:
            new_asteroids.append(asteroid)

    asteroids = new_asteroids

# -------------------------
# Create a laser
# -------------------------
def spawn_laser():

    # Create a rectangle for the new laser
    laser = laser_image.get_rect()

    # Start the laser at the player's position
    laser.center = player_rect.center

    # Add the laser to the list
    lasers.append(laser)

    # Play the laser sound
    laser_sound.play()

# -------------------------
# Create an asteroid
# -------------------------
def spawn_asteroid():

    # Create a rectangle for the new asteroid
    asteroid = asteroid_image.get_rect()

    # Pick a random x position
    xpos = random.randint(
        asteroid.width,
        WIDTH - asteroid.width
    )

    # Put the asteroid just above the screen
    asteroid.midbottom = (xpos, 0)

    # Add it to the list
    asteroids.append(asteroid)

# -------------------------
# Start the game
# -------------------------
def start_game():

    global current_state
    global asteroid_timer
    global thruster_timer
    global thruster_frame
    global thruster_direction

    current_state = GAME

    # Reset timers
    asteroid_timer = 0
    thruster_timer = 0

    # Reset the thruster animation
    thruster_frame = 0
    thruster_direction = 1

# -------------------------
# Update the game
# -------------------------
def update(dt):

    global asteroid_timer
    global thruster_timer

    if current_state == GAME:

        # Check the left and right keys
        check_keys(dt)

        # Move the thruster
        move_thrusters()

        # Move lasers and asteroids
        move_lasers(dt)
        move_asteroids(dt)

        # Check for collisions
        check_laser_collisions()
        check_player_collisions()

        # Remove objects that leave the screen
        clean_up()

        # -------------------------
        # Asteroid timer
        # -------------------------

        asteroid_timer += dt

        if asteroid_timer >= 0.5:

            spawn_asteroid()

            # Reset the timer
            asteroid_timer = 0

        # -------------------------
        # Thruster timer
        # -------------------------

        thruster_timer += dt

        if thruster_timer >= 0.2:

            animate_thrusters()

            # Reset the timer
            thruster_timer = 0

# -------------------------
# Handle events
# -------------------------
def handle_events():

    global current_state

    for event in pygame.event.get():

        # Close the window
        if event.type == pygame.QUIT:
            return False


        # Keyboard key pressed
        if event.type == pygame.KEYDOWN:

            # Enter starts or restarts the game
            if event.key == pygame.K_RETURN:

                if (
                    current_state == TITLE
                    or current_state == GAMEOVER
                ):
                    start_game()


            # Space shoots a laser
            elif event.key == pygame.K_SPACE:

                if (
                    current_state == GAME
                    and len(lasers) < 4
                ):
                    spawn_laser()


            # Escape quits the game
            elif event.key == pygame.K_ESCAPE:

                return False

    return True

# -------------------------
# Main game loop
# -------------------------
running = True

while running:

    # Time since the previous frame
    milliseconds = clock.tick(60)
    dt = milliseconds / 1000

    # Handle keyboard and window events
    running = handle_events()

    # Update the game
    update(dt)

    # Draw everything
    draw()

    # Show the completed frame
    pygame.display.flip()


pygame.quit()
sys.exit()
