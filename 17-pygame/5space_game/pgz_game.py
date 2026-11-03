# Necessary for pygame zero
import pgzrun

# Used to generate random integers
import random

# Used for Quitting the Program
import sys

# Window Properties
TITLE = 'SPACE!!!'
WIDTH = 800
HEIGHT = 800

# Title Screen as an "Actor"
game = Actor('game-title')
game.midtop = (400,200)
game.state = ['title', 'game', 'gameover']
game.current_state = game.state[0]

# Play spaceship
player = Actor('pixel_ship_blue')
player.pos = (WIDTH // 2, HEIGHT - 100)

# Animated Thruster that shows at the bottom of the spaceship
thrusters = Actor('thruster-1')
thrusters.frames = ['thruster-1', 'thruster-2', 'thruster-3', 'thruster-4']
thrusters.pos = player.midbottom
thrusters.current_frame = 0
thrusters.direction = 1

# List of lasers fired by player
lasers = []
# List of asteroids active
asteroids = []

# Draw the background on the screen
def draw_background():
    # Tile that background due to the small image size
    for x in range(0, 800, 400):
        for y in range(0, 800, 400):
            screen.blit('background-purple', (x, y))
            
# Draw the main menu Screen
def draw_main_menu():
    game.draw()
    screen.blit('press-enter', (300, 500))
    
# Draw the game over Screen
def draw_game_over():
    screen.blit('game-over', (200, 200))
    screen.blit('press-enter', (300, 500))

# Draw lasers the player shoots
def draw_lasers():
    global lasers
    for laser in lasers:
        laser.draw()

# Draw active asteroids
def draw_asteroids():
    global asteroids
    for asteroid in asteroids:
        asteroid.draw()

# Draw function provided by pygame zero
def draw():
    
    # Draw the background first so other things
    #   are drawn on top it
    draw_background()
    
    # Show the main menu based on the game's "state"
    if game.current_state == 'title':
        draw_main_menu()
    
    # Draw the player and game stuff when we are
    #  actively playing the game
    elif game.current_state == 'game':
        draw_lasers()
        thrusters.draw()
        player.draw()
        draw_asteroids()
    
    # Uh oh...game over...
    elif game.current_state == 'gameover':
        draw_game_over()

# During the "game" state check for the left and right keys
#   we do this because they can be held down to move
def check_keys(dt):
    if game.current_state == 'game':
        if keyboard.LEFT:
            player.x -= dt * 300
            if player.left < 0:
                player.left = 0
        if keyboard.RIGHT:
            player.x += dt * 300
            if player.right > WIDTH:
                player.right = WIDTH

# Function to switch the animation frames of the thrusters
def animate_thrusters():
    # It counts up and then back down repeatedly
    if not (0 <= thrusters.current_frame + thrusters.direction < len(thrusters.frames)):
        thrusters.direction *= -1    
    
    thrusters.current_frame += thrusters.direction
    thrusters.image = thrusters.frames[thrusters.current_frame]

# Reposition the thrusters to the location of the player ship
def move_thrusters():
    thrusters.midtop = player.midbottom

# Move the lasers toward the top of the screen
def move_lasers(dt):
    global lasers
    for laser in lasers:
        laser.y -= dt * 400

# Move the asteroids toward the bottom of the screen
def move_asteroids(dt):
    global asteroids
    for asteroid in asteroids:
        asteroid.y += dt * 400

# Check if the laser has hit any asteroids
def check_laser_collisions():
    global lasers
    global asteroids
    # Check all lasers
    for laser in lasers:
        # Check all asteroids
        for asteroid in asteroids:
            # Did the laser hit the asteroid?
            if laser.colliderect(asteroid):
                # If so, we set these properties to False
                #   to cleanup the laser and the asteroid it hit
                laser.render = False
                asteroid.render = False
                # Play a fun 'spolde sound
                sounds.explode.play()

# Check if the player hit anything
def check_player_collisions():
    global asteroids
    global lasers
    # Check all asteroids
    for asteroid in asteroids:
        # Did the player hit the asteroid?
        if player.colliderect(asteroid):
            # If so...game over state
            game.current_state = game.state[2]
            # Play the explosion sound
            sounds.explode.play()
            # Stop spawning asteroids
            clock.unschedule(spawn_asteroid)
            # Stop animating the thrusters
            clock.unschedule(animate_thrusters)
            # Reset the thruster frame to the first frame
            animate_thrusters.current_frame = 0
            # Empty the asteroid and laser lists
            asteroids = []
            lasers = []           

# This runs 60 times a second and is provided by pygame zero
#   The dt paramter is the time difference between the last time
#   this function was run. We can use it to smooth out sprite movements
def update(dt):
    check_keys(dt)
    move_thrusters()
    move_lasers(dt)
    move_asteroids(dt)
    check_laser_collisions()
    check_player_collisions()
    clean_up()

# Get rid of any lasers or asteroids that shouldn't be drawn any more
def clean_up():
    global lasers
    global asteroids
    new_lasers = []
    # Check all laser
    for laser in lasers:
        # If the bottom of the laser is not past the top
        #   of the screen and the laser.render is set to True
        if not laser.bottom < 0 and laser.render:
            # Keep the laser
            new_lasers.append(laser)
    # Update the list of lasers
    lasers = new_lasers
    
    # Repeat the above process for the asteroids
    new_asteroids = []
    for asteroid in asteroids:
        # If the top of the asteroid is not below the bottom
        #   of the screen and asteroid.render is set to True
        if not asteroid.top > HEIGHT and asteroid.render:
            new_asteroids.append(asteroid)
    asteroids = new_asteroids

# Create a laser
def spawn_laser():
    global lasers
    
    # Create the Actor and use the laser image
    laser = Actor('pixel_laser_blue')
    
    # Set the laser position to be the same as the player
    laser.pos = (player.x, player.y)
    
    # Set a custom variable to remember to render (draw) it
    laser.render = True
    
    # Add it to the list of lasers
    lasers.append(laser)
    
    # Play our pewpew sound
    sounds.laser.play()

# Create a asteroid
def spawn_asteroid():
    global asteroids
    
    # Create the Actor and use the asteroid image
    asteroid = Actor('asteroid_grey')
    
    # Pick a random x position on the screen to draw the asteroid
    xpos = random.randint(asteroid.width, WIDTH - asteroid.width)
    
    # Draw the bottom of the asteroid at y value 0
    #   (makes it slightly off screen) 
    asteroid.midbottom = (xpos, 0)
    
    # Set a custom variable to remember to render (draw) it
    asteroid.render = True
    
    # Add it to the list of asteroids
    asteroids.append(asteroid)

# Function provided by pygame zero to check for keyboard presses
def on_key_down(key):
    # We only care are certain keys if we are in the title or
    #   gameover states (namely the return key)
    if game.current_state == 'title' or game.current_state == 'gameover':
        if key == keys.RETURN:
            # Change the state to be "game"
            game.current_state = game.state[1]
            # Start the asteroid spawning every .5 seconds
            clock.schedule_interval(spawn_asteroid, 0.5)
            # Start the animation of the thrusters ever .2 secons
            clock.schedule_interval(animate_thrusters, 0.2)
    # If we press the spacebar and we are playing the game AND we haven't already
    #   fired four lasers.
    elif key == keys.SPACE and game.current_state == 'game' and len(lasers) < 4:
        # Shoot a laser
        spawn_laser()
    
    # Check for escape key press
    if key == keys.ESCAPE:
        # Exit the program
        sys.exit()
   
# Start pygame zero
pgzrun.go()
