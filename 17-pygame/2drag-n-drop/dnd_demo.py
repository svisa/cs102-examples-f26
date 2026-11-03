
import sys
import pygame

# -------------------------
# Setup
# -------------------------

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag the Alien")

clock = pygame.time.Clock()

# Load the images;
#convert_alpha draws faster an image with transparent background faster
alien_image = pygame.image.load("images/alien.png").convert_alpha()
alien_drag_image = pygame.image.load("images/alien_drag.png").convert_alpha()

# Start the alien in the center of the screen
alien_x = WIDTH // 2
alien_y = HEIGHT // 2

# Variables to track dragging
dragging = False
offset_x = 0
offset_y = 0


# -------------------------
# Draw everything
# -------------------------

def draw():
    screen.fill((200, 200, 255))

    # Use the drag image while dragging
    if dragging:
        screen.blit(alien_drag_image, (alien_x, alien_y))
    else:
        screen.blit(alien_image, (alien_x, alien_y))


# -------------------------
# Handle mouse events
# -------------------------

def handle_mouse_events(event):
    global alien_x, alien_y
    global dragging, offset_x, offset_y

    # Mouse button pressed
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        # Get the alien's rectangle
        alien_rect = alien_image.get_rect(topleft=(alien_x, alien_y))

        # Check if the mouse clicked on the alien
        if alien_rect.collidepoint(mouse_x, mouse_y):
            dragging = True

            # Remember where on the alien the mouse was clicked
            offset_x = mouse_x - alien_x
            offset_y = mouse_y - alien_y

    # Mouse button released
    elif event.type == pygame.MOUSEBUTTONUP:
        dragging = False

    # Mouse moved
    elif event.type == pygame.MOUSEMOTION:
        if dragging:
            mouse_x, mouse_y = event.pos

            # Move the alien while keeping the same
            # point under the mouse
            alien_x = mouse_x - offset_x
            alien_y = mouse_y - offset_y


# -------------------------
# Main program
# -------------------------

running = True

while running:

    # Check for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        else:
            handle_mouse_events(event)

    # Draw the screen
    draw()

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 frames per second
    clock.tick(60)

pygame.quit()
sys.exit() #closes window

