# with functions
# Explorer and Zombie animation - written with plain pygame
#
# Folder layout this program expects:
#   explorer_zombie_pygame.py
#   images/
#       idle.png, walk037.png ... walk043.png
#       zwalk037.png ... zwalk043.png
#       emote_dots1.png, emote_dots2.png, emote_dots3.png
#       emote_exclamation.png
#       bgforest_small.png
#
# (These are the same images the Pygame Zero version used.
#  If yours are .jpg or another type, change the file endings below.)

import sys
import pygame

# ----------------------------------------------------------------
# SETUP
# ----------------------------------------------------------------
# Pygame Zero did this for us. In pygame we do it ourselves.
pygame.init()

WIDTH = 640
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explorer and Zombie")

# A Clock lets us run the game at a steady speed (60 frames per second)
# and tells us how much time has passed between frames.
clock = pygame.time.Clock()


# ----------------------------------------------------------------
# LOADING IMAGES
# ----------------------------------------------------------------
# Pygame Zero loaded images from the "images" folder by name.
# In pygame we load each image file ourselves.
def load_image(name):
    # convert_alpha() keeps the transparent parts of the picture
    # and makes drawing faster.
    return pygame.image.load("images/" + name + ".png").convert_alpha()


background = pygame.image.load("images/bgforest_small.png").convert()

explorer_idle = load_image("idle")
explorer_walk_images = []
for name in ["walk037", "walk038", "walk039", "walk040",
             "walk041", "walk042", "walk043"]:
    explorer_walk_images.append(load_image(name))

zombie_walk_images = []
for name in ["zwalk037", "zwalk038", "zwalk039", "zwalk040",
             "zwalk041", "zwalk042", "zwalk043"]:
    zombie_walk_images.append(load_image(name))

emote_dots_images = [load_image("emote_dots1"),
                     load_image("emote_dots2"),
                     load_image("emote_dots3")]
emote_exclaim_image = load_image("emote_exclamation")


# ----------------------------------------------------------------
# GAME VARIABLES
# ----------------------------------------------------------------
# The current "state" (stage) of the animation:
#   0 = explorer walks to the middle of the screen
#   1 = explorer stops, zombie appears and walks closer
#   2 = explorer and zombie both run off screen
current_state = 0

SPEED = 20  # pixels per second

# Positions. (x, y) is the CENTER of each picture, just like
# the Actor positions in Pygame Zero.
explorer_x = -50
explorer_y = 400
zombie_x = -50
zombie_y = 400

# The image currently showing for each character
explorer_image = explorer_walk_images[0]
zombie_image = zombie_walk_images[0]
emote_image = emote_dots_images[0]

# The emote only shows once it has been placed above the explorer
emote_x = None
emote_y = None

# Which frame of each animation we are on
walk_frame = 0
zwalk_frame = 0
emote_frame = 0

# ----------------------------------------------------------------
# TIMERS
# ----------------------------------------------------------------
# Pygame Zero had clock.schedule_interval(). In pygame we make our own:
# each timer counts up the seconds that pass. When it reaches its
# interval, we change the animation frame and reset the timer.
explorer_timer = 0
zombie_timer = 0
emote_timer = 0

# Flags that turn each animation on or off
explorer_animating = True    # the explorer starts out walking
zombie_animating = False
emote_animating = False


# ----------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------
def draw_centered(image, x, y):
    # blit() draws an image with its TOP-LEFT corner at the position
    # you give it. This helper puts the CENTER there instead,
    # so positions work like Actors did in Pygame Zero.
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)


def update_animations(dt):
    # Change picture frames when each timer runs out.
    # "global" lets a function change variables defined outside it.
    global explorer_timer, zombie_timer, emote_timer
    global walk_frame, zwalk_frame, emote_frame
    global explorer_image, zombie_image, emote_image
    global emote_x, emote_y

    # --- Explorer walk cycle (every 0.2 seconds) ---
    if explorer_animating:
        explorer_timer += dt
        if explorer_timer >= 0.2:
            explorer_timer = 0
            # % (mod) keeps the frame number between 0 and the list length
            explorer_image = explorer_walk_images[walk_frame % len(explorer_walk_images)]
            walk_frame += 1

    # --- Zombie walk cycle (every 0.2 seconds) ---
    if zombie_animating:
        zombie_timer += dt
        if zombie_timer >= 0.2:
            zombie_timer = 0
            zombie_image = zombie_walk_images[zwalk_frame % len(zombie_walk_images)]
            zwalk_frame += 1

    # --- Emote above the explorer's head (every 0.5 seconds) ---
    if emote_animating:
        emote_timer += dt
        if emote_timer >= 0.5:
            emote_timer = 0
            # Put the emote above the explorer's head
            emote_x = explorer_x
            emote_y = explorer_y - 50

            if zombie_x < explorer_x // 2:
                # Zombie is still far away: show the "..." animation
                emote_image = emote_dots_images[emote_frame % len(emote_dots_images)]
                emote_frame += 1
            else:
                # Zombie is close: show the exclamation mark
                emote_image = emote_exclaim_image


def update_state(dt):
    # Controls the sequence of events in the animation
    global current_state, explorer_x, zombie_x
    global explorer_animating, zombie_animating, emote_animating
    global explorer_image, explorer_timer, emote_timer, zombie_timer

    if current_state == 0:
        # Has the explorer reached the middle of the screen?
        if explorer_x > WIDTH // 2:
            # Stop walking and stand still
            explorer_animating = False
            explorer_image = explorer_idle

            # Start the emote and the zombie
            emote_animating = True
            zombie_animating = True
            emote_timer = 0
            zombie_timer = 0

            current_state = 1
        else:
            # Not there yet, so keep moving right
            explorer_x += SPEED * dt

    elif current_state == 1:
        # Is the zombie still more than 150 pixels from the explorer?
        if zombie_x < explorer_x - 150:
            zombie_x += SPEED * dt
        else:
            # Zombie is close enough: stop the emote and start
            # the explorer walking (running away!) again
            emote_animating = False
            explorer_animating = True
            explorer_timer = 0

            current_state = 2

    else:
        # Final state: both run off the screen.
        # (This state continues until you close the window.)
        explorer_x += SPEED * dt
        zombie_x += SPEED * dt


def draw():
    # Draw the background FIRST so everything else appears on top
    screen.blit(background, (0, 0))

    # Explorer is always drawn
    draw_centered(explorer_image, explorer_x, explorer_y)

    if current_state == 1:
        # Only draw the emote once it has been placed above the head
        if emote_x is not None:
            draw_centered(emote_image, emote_x, emote_y)
        draw_centered(zombie_image, zombie_x, zombie_y)

    elif current_state == 2:
        draw_centered(zombie_image, zombie_x, zombie_y)

    # Show everything we just drew on the actual window
    pygame.display.flip()


# ----------------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------------
# Pygame Zero called update() and draw() for us automatically.
# In pygame we write the loop ourselves.
running = True
while running:
    # dt = seconds since the last frame (limits the game to 60 FPS)
    dt = clock.tick(60) / 1000

    # Check for events, like the player closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_state(dt)
    update_animations(dt)
    draw()

pygame.quit()
sys.exit()