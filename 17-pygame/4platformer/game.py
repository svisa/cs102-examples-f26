# game that follows the recepie draw → handle movement →
# check the ground → repeat.
import sys
import pygame

# -------------------------
# Setup
# -------------------------

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JUMP PERSON")

clock = pygame.time.Clock()


# -------------------------
# Load images
# -------------------------

platform_image = pygame.image.load(
    "images/stage/platform.png"
).convert_alpha()

player_images = [
    pygame.image.load("images/player/tile_0000.png").convert_alpha(),
    pygame.image.load("images/player/tile_0001.png").convert_alpha()
]


# -------------------------
# Create platforms
# -------------------------

platforms = [
    platform_image.get_rect(
        midtop=(WIDTH // 2, HEIGHT // 2)
    ),

    platform_image.get_rect(
        midtop=(WIDTH // 2 + 200, HEIGHT // 2 + 50)
    ),

    platform_image.get_rect(
        midtop=(WIDTH // 2 - 200, HEIGHT // 2 + 50)
    )
]


# -------------------------
# Create player
# -------------------------

player_image = player_images[0]

player_rect = player_image.get_rect()
player_rect.midbottom = platforms[0].midtop

grounded = True
impulse = 0


# -------------------------
# Draw everything
# -------------------------

def draw():
    screen.fill((0, 0, 0))

    # Choose the player image
    if grounded:
        image = player_images[0]
    else:
        image = player_images[1]

    screen.blit(image, player_rect)

    draw_platforms()


def draw_platforms():
    for platform in platforms:
        screen.blit(platform_image, platform)


# -------------------------
# Check if player is on a platform
# -------------------------

def ground_check():
    global grounded
    global impulse

    grounded = False

    for platform in platforms:

        if player_rect.colliderect(platform):

            # Put the bottom of the player
            # at the top of the platform
            player_rect.bottom = platform.top

            grounded = True
            impulse = 0


# -------------------------
# Move the player
# -------------------------

def player_movement(dt):
    global impulse

    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(dt * 100)

    # Move right
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(dt * 100)

    # Apply gravity
    if not grounded:
        impulse -= 10.8
        player_rect.y -= int(dt * impulse)

    # If the player falls off the screen,
    # move them back to the top
    if player_rect.top > HEIGHT:
        player_rect.top = 0


# -------------------------
# Handle key presses
# -------------------------

def handle_events():
    global grounded
    global impulse

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:

            # Jump
            if event.key == pygame.K_SPACE and grounded:
                grounded = False
                impulse = 400

            # Quit
            if event.key == pygame.K_ESCAPE:
                return False

    return True


# -------------------------
# Update the game
# -------------------------

def update(dt):
    player_movement(dt)
    ground_check()


# -------------------------
# Main game loop
# -------------------------

running = True

while running:

    # Calculate time since the previous frame
    milliseconds = clock.tick(60)
    dt = milliseconds / 1000

    running = handle_events()

    update(dt)

    draw()

    pygame.display.flip()


pygame.quit()
sys.exit()


