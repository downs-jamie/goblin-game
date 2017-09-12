# 1. Include pygame
# Include pygame which we got from pip
import pygame

# from the math module (built into python), get the fabs method
from math import fabs
# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()

# 3. Create a screen with a particular size
# the screen size MUST be a tuple

screen_size_x = 512
screen_size_y = 480


screen_size = (screen_size_x,screen_size_y)
# Tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)


# Actually tell pygame to set the screen up and store it



# Set a pointless caption
pygame.display.set_caption("Goblin Chase")
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




def keepCharInBounds(character):
    if character['y'] < 0:
            character['y'] = 0
    elif character['y'] + 32 >= screen_size_y:
            character['y'] = screen_size_y - 32

    if character['x'] < 0:
        character['x'] = 0
    elif character['x'] + 32 >= screen_size_x:
        character['x'] = screen_size_x - 32

def pointMe (yourPosition, goalPosition):
    # print yourPosition
    # print goalPosition
    delta = [0,0]
    delta[0] = yourPosition[0] - goalPosition[0]
    delta[1] = yourPosition[1] - goalPosition[1]
    # lineDistance = sqrt((pow(delta[0],2)) + (pow(delta[1],2)))
    # print lineDistance
    return delta

def randomlyPlaceChar(character):
    golbli['x'] = random.randint(32,screen_size_x - 32)
    goblin['y'] = random.randint(32,screen_size_y - 32)
    return (character['x'], character['y'])

def removeObjectFromBackground(object):
        pygame_screen.blit(background_image, (object['x'], object['y']), pygame.Rect(object['x'], object['y'], object['height'], object['width']))
        object['x'] = screen_size_x + 100
        object['y'] = screen_size_y + 100
        return (object['x'],object['y'])

def detectCollision(character1, character2):
    distance_between = fabs(character1['x'] - character2['x']) + fabs(character1['y'] - character2['y'])

    if distance_between < 32:
        return True

    return (False)


def moveLordVader(character, pursue=True):
    # Move Vader either towards or away from character depending on bool
    # default is to pursue, when pursue is false we evade

    # Use pointMe to get the deltas for calculating slope
    target = pointMe([hero['x'],hero['y']], [hero['x'],hero['y']])

    # TODO Ask why I have to do global here but NOT above
    global lordVader_image

    # Setting x coordinate is easy...based on sign and speed
    if pursue:
        if target[0] < 0:  # delta x
            lordVader_image = lordVaderImageRight
            lordVader['x'] += lordVader['speed']
        elif target[0] > 0:
            lordVader_image = lordVaderImageLeft
            lordVader['x'] -= lordVader['speed']
        else:
            # print "Collision Along X"
            #kluge....avoid potential divide by zero error!
            target[0] = 1
    else: # need to evade, reverse everthing above
        if target[0] < 0:  # delta x
            lordVader_image = lordVaderImageLeft
            lordVader['x'] -= lordVader['speed']
        elif target[0] > 0:
            lordVader_image = lordVaderImageRight
            lordVader['x'] += lordVader['speed']
        else:
            # print "Collision Along X"
            #kluge....avoid potential divide by zero error!
            target[0] = 1

    # y coordinate is tougher...speed is a proxy for distance
    # we know slope so ratio should hold along the hypotenuse (goal path)...
    # y is "speed" we're looking for...

    if pursue:
        if target[0] <= 32:
            if target[1] <= 0:
                lordVader['y'] += lordVader['speed']
            else:
                lordVader['y'] -= lordVader['speed']
        elif target[1] < 0:  # delta y
            lordVader['y'] += round(fabs(lordVader['speed']*target[1]/target[0]))
        elif target[1] > 0:
            lordVader['y'] -= round(fabs(lordVader['speed']*target[1]/target[0]))
        # else:  delta Y is 0
        #     print "Collision Along Y"
    else: #evade...opposite of above
        if target[0] <= 32:  # already collided along X
            if target[1] <= 0:
                lordVader['y'] -= lordVader['speed']
            else:
                lordVader['y'] += lordVader['speed']
        elif target[1] < 0:  # delta y
            lordVader['y'] -= round(fabs(lordVader['speed']*target[1]/target[0]))
        elif target[1] > 0:
            lordVader['y'] += round(fabs(lordVader['speed']*target[1]/target[0]))
        # else:  Delta Y is zero
        #     print "Collision Along Y"
        #kluge to the 4 corners problem...
        if ((detectCollision(lordVader, topLeftCorner)) or
        (detectCollision(lordVader, topRightCorner)) or
        (detectCollision(lordVader, bottomLeftCorner)) or
        (detectCollision(lordVader, bottomRightCorner))):
            randomlyPlaceChar(lordVader)

    #print "After Y-Speed calc...Lord Vader x: %r y: %r" % (lordVader['x'], lordVader['y'])
    keepCharInBounds(lordVader)

# 4. Create a game loop (while)
# Create a boolean for whether the game should be going or not
game_on = True
while game_on:
	


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