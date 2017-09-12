# 1. Include pygame
# Include pygame which we got from pip
import pygame
import random
# from the math module (built into python), get the fabs method
from math import fabs
# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()
pygame.mixer.init()
# 3. Create a screen with a particular size
# the screen size MUST be a tuple

screen_size_x = 512
screen_size_y = 480
FPS = 30

screen_size = (screen_size_x,screen_size_y)

# Tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)


# Actually tell pygame to set the screen up and store it



# Set a pointless caption
pygame.display.set_caption("Goblin Chase")

clock = pygame.time.Clock()

# set up a var with our image
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')
acorn_image = pygame.image.load('acorn.png')
screen = pygame.mixer.music.load('sounds/08 Intermission.mp3')
pygame.mixer.music.play(-1, 0.0)


# 8. Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}

goblin = {
	"x": 400,
	"y": 200,
	"speed": 15
}

monster = {
	"x": 100,
	"y": 400,
	"speed": 19
	
}

acorn = {
	"x": 449,
	"y": 412,
	
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}






# 4. Create a game loop (while)
# Create a boolean for whether the game should be going or not
game_on = True
while game_on:
	clock.tick(FPS)
# process input (events)

# update
# draw / render

	# we are inside the main game loop.
	# it will keep running, as long as our bool is true
	# 5. Add a quit event (Python needs an escape)
	# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			# the user clicked the red x in the top left
			game_on = False
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			if event.key == keys['up']:
				# user pressed up!!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys['down']:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys['left']:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			elif event.key == keys['right']:
				# hero['x'] += hero['speed']
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# the user let go of a key. See if it's one that matters
			if event.key == keys['up']:
				# user let go of the upkey. Flip the bool
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False

	
		

	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	
	
	
	
	
	# COLLISION DETECTION!!!
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32:
		# the hero and goblin are touching!
		print "collision!"

	distance_between = fabs(hero['x'] - acorn['x']) + fabs(hero['y'] - acorn['y'])
	if distance_between < 32:
		# the hero and goblin are touching!
		print "collision!"



				

	# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you watn you to draw it
	pygame_screen.blit(background_image, [0,0])

	# Make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])
	
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])
	pygame_screen.blit(monster_image, [monster['x'],monster['y']])
	pygame_screen.blit(acorn_image, [acorn['x'],acorn['y']])
	# 7. Repeat 6 over and over over...
	pygame.display.flip()


pygame.quit()	