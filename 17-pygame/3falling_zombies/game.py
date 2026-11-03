
# Need to install pygame before running this program.
# In Thonny, install pygame using Tools -> Manage packages.
import sys
import pygame
import random


# --------------------------------------------------
# Set up Pygame
# --------------------------------------------------

pygame.init()

TITLE = "ZOMBIE DROP"

WIDTH = 640
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


# --------------------------------------------------
# Load images
# --------------------------------------------------

background = pygame.image.load("images/bggrass.png")

explorer_image = pygame.image.load("images/eidle.png")
zombie_image = pygame.image.load("images/zombie.png")
heart_image = pygame.image.load("images/heart.png")


# --------------------------------------------------
# Create the explorer
# --------------------------------------------------

explorer_x = 100
explorer_y = 500

explorer_width = explorer_image.get_width()
explorer_height = explorer_image.get_height()

explorer_lives = 3
explorer_invincible = False

# Timer used after the explorer is hit
invincible_timer = 0


# --------------------------------------------------
# Create the hearts
# --------------------------------------------------

hearts = []

for number in range(3):

    heart_x = WIDTH - (33 * (2 - number)) - 3
    heart_y = HEIGHT - heart_image.get_height() - 3

    hearts.append(
        (heart_x, heart_y)
    )


# --------------------------------------------------
# Create the zombie list
# --------------------------------------------------

zombies = []


# --------------------------------------------------
# Game state
# --------------------------------------------------

TITLE_SCREEN = 0
GAMEPLAY = 1
GAME_OVER = 2

current_state = TITLE_SCREEN


# --------------------------------------------------
# Game difficulty
# --------------------------------------------------

difficulty = 60


# Timer for creating zombies
spawn_timer = 0

# Timer for increasing difficulty
difficulty_timer = 0


# --------------------------------------------------
# Fonts
# --------------------------------------------------

title_font = pygame.font.Font(None, 70)
message_font = pygame.font.Font(None, 25)


# --------------------------------------------------
# Show the title screen
# --------------------------------------------------

def show_title_screen():

    title_text = title_font.render(
        "Zombie Drop",
        True,
        (0, 0, 0)
    )

    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, 130)

    screen.blit(title_text, title_rect)


    message_text = message_font.render(
        "Press Any Key to Start",
        True,
        (0, 0, 0)
    )

    message_rect = message_text.get_rect()
    message_rect.center = (WIDTH // 2, HEIGHT - 100)

    screen.blit(message_text, message_rect)


# --------------------------------------------------
# Show the game-over screen
# --------------------------------------------------

def show_gameover():

    title_text = title_font.render(
        "Game Over",
        True,
        (0, 0, 0)
    )

    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, 130)

    screen.blit(title_text, title_rect)


    message_text = message_font.render(
        "Press Any Key to Start",
        True,
        (0, 0, 0)
    )

    message_rect = message_text.get_rect()
    message_rect.center = (WIDTH // 2, HEIGHT - 100)

    screen.blit(message_text, message_rect)


# --------------------------------------------------
# Draw the game
# --------------------------------------------------

def draw():

    # Draw the background first
    screen.blit(background, (0, 0))


    # ----------------------------------------------
    # Title screen
    # ----------------------------------------------

    if current_state == TITLE_SCREEN:

        show_title_screen()


    # ----------------------------------------------
    # Gameplay
    # ----------------------------------------------

    elif current_state == GAMEPLAY:

        # Draw every zombie
        for zombie in zombies:

            screen.blit(
                zombie_image,
                (zombie["x"], zombie["y"])
            )


        # Draw the explorer
        screen.blit(
            explorer_image,
            (explorer_x, explorer_y)
        )


        # Draw the hearts
        draw_hearts()


    # ----------------------------------------------
    # Game over
    # ----------------------------------------------

    elif current_state == GAME_OVER:

        show_gameover()


    # Show everything that has been drawn
    pygame.display.flip()


# --------------------------------------------------
# Draw the hearts
# --------------------------------------------------

def draw_hearts():

    for number in range(explorer_lives):

        x, y = hearts[number]

        screen.blit(
            heart_image,
            (x, y)
        )


# --------------------------------------------------
# Move the explorer
# --------------------------------------------------

def check_keys(dt):

    global explorer_x

    # Get the keys that are currently being held down
    keys = pygame.key.get_pressed()


    # Move left
    if keys[pygame.K_LEFT]:

        explorer_x -= dt * 100


    # Move right
    if keys[pygame.K_RIGHT]:

        explorer_x += dt * 100


    # Keep the explorer on the screen
    if explorer_x < 0:

        explorer_x = 0

    if explorer_x + explorer_width > WIDTH:

        explorer_x = WIDTH - explorer_width


# --------------------------------------------------
# Create a new zombie
# --------------------------------------------------

def spawn_zombie():

    # Choose a random x position
    xpos = random.randint(50, WIDTH - 50)


    # Create a dictionary to store the zombie's information
    zombie = {
        "x": xpos,
        "y": -50,
        "alive": True
    }


    # Add the zombie to the list
    zombies.append(zombie)


# --------------------------------------------------
# Move the zombies
# --------------------------------------------------

def move_zombies(dt):

    global difficulty

    for zombie in zombies:

        # Move the zombie down
        zombie["y"] += dt * difficulty


        # Has the zombie moved below the screen?
        if zombie["y"] > HEIGHT + 100:

            zombie["alive"] = False


# --------------------------------------------------
# Remove zombies that are no longer needed
# --------------------------------------------------

def zombie_cleanup():

    global zombies

    # Make a new list
    new_list = []


    # Keep only zombies that are still alive
    for zombie in zombies:

        if zombie["alive"]:

            new_list.append(zombie)


    # Replace the old list
    zombies = new_list


# --------------------------------------------------
# Check for collisions
# --------------------------------------------------

def check_zombie_collision():

    global explorer_lives
    global explorer_invincible
    global invincible_timer


    # Create a rectangle around the explorer
    explorer_rect = pygame.Rect(
        explorer_x,
        explorer_y,
        explorer_width,
        explorer_height
    )


    # Check every zombie
    for zombie in zombies:

        zombie_rect = pygame.Rect(
            zombie["x"],
            zombie["y"],
            zombie_image.get_width(),
            zombie_image.get_height()
        )


        # Did the zombie hit the explorer?
        if (
            not explorer_invincible
            and explorer_rect.colliderect(zombie_rect)
        ):

            # Lose one life
            explorer_lives -= 1


            # Make the explorer temporarily invincible
            explorer_invincible = True

            # Stay invincible for 5 seconds
            invincible_timer = 5


# --------------------------------------------------
# Update the invincibility timer
# --------------------------------------------------

def update_invincibility(dt):

    global explorer_invincible
    global invincible_timer


    if explorer_invincible:

        invincible_timer -= dt


        # Has the 5 seconds passed?
        if invincible_timer <= 0:

            explorer_invincible = False


# --------------------------------------------------
# Increase the difficulty
# --------------------------------------------------

def increase_challenge():

    global difficulty

    difficulty += 60


# --------------------------------------------------
# Start the game
# --------------------------------------------------

def start_game():

    global current_state
    global explorer_lives
    global difficulty
    global spawn_timer
    global difficulty_timer
    global explorer_x
    global explorer_invincible
    global invincible_timer


    # Change to gameplay
    current_state = GAMEPLAY


    # Reset the explorer
    explorer_lives = 3
    explorer_x = 100

    explorer_invincible = False
    invincible_timer = 0


    # Reset the difficulty
    difficulty = 60


    # Reset the timers
    spawn_timer = 0
    difficulty_timer = 0


    # Remove any old zombies
    zombies.clear()


# --------------------------------------------------
# Update the game
# --------------------------------------------------

def update(dt):

    global current_state
    global spawn_timer
    global difficulty_timer


    # Only update the game during gameplay
    if current_state != GAMEPLAY:

        return


    # ----------------------------------------------
    # Move the explorer
    # ----------------------------------------------

    check_keys(dt)


    # ----------------------------------------------
    # Move the zombies
    # ----------------------------------------------

    move_zombies(dt)


    # ----------------------------------------------
    # Check for collisions
    # ----------------------------------------------

    check_zombie_collision()


    # ----------------------------------------------
    # Update invincibility
    # ----------------------------------------------

    update_invincibility(dt)


    # ----------------------------------------------
    # Create zombies every 5 seconds
    # ----------------------------------------------

    spawn_timer += dt

    if spawn_timer >= 5:

        spawn_zombie()

        spawn_timer = 0


    # ----------------------------------------------
    # Increase difficulty every 30 seconds
    # ----------------------------------------------

    difficulty_timer += dt

    if difficulty_timer >= 30:

        increase_challenge()

        difficulty_timer = 0


    # ----------------------------------------------
    # Remove zombies that have left the screen
    # ----------------------------------------------

    zombie_cleanup()


    # ----------------------------------------------
    # Check for game over
    # ----------------------------------------------

    if explorer_lives == 0:

        current_state = GAME_OVER


# --------------------------------------------------
# Handle keyboard and other events
# --------------------------------------------------

def handle_events():

    global current_state


    for event in pygame.event.get():

        # Did the player close the window?
        if event.type == pygame.QUIT:

            return False


        # Did the player press a key?
        if event.type == pygame.KEYDOWN:

            # Escape quits the game
            if event.key == pygame.K_ESCAPE:

                return False


            # Any other key starts the game
            elif current_state == TITLE_SCREEN:

                start_game()


            # Any other key restarts after game over
            elif current_state == GAME_OVER:

                start_game()


    return True


# --------------------------------------------------
# Main game loop
# --------------------------------------------------

running = True

while running:

    # Find out how much time has passed
    milliseconds = clock.tick(60)

    # Convert milliseconds to seconds
    dt = milliseconds / 1000


    # Check for keyboard and window events
    running = handle_events()


    # Update the game
    update(dt)


    # Draw the game
    draw()


# --------------------------------------------------
# Quit Pygame
# --------------------------------------------------

pygame.quit()
sys.exit()


