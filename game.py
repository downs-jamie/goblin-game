# 1include pygame
# 2init pygame
import pygame
pygame.init()
# 3create screen with ? size
screen_size = (512,480)

#must be tuple
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
#set hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20
}
keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left":276
}
# 4create a.game loop (while)
#create a boolean for whether the game should be 
game_on = True
while game_on:

# 5add a guit event (python needs a escape
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				hero['y'] += hero['speed']
			elif event.key == keys['left']:
				hero['x'] -= hero['speed']
			elif event.key == keys['right']:
				hero['x'] += hero['speed']		
				

				
# 6fill in the screen with a color or image)
	pygame_screen.blit(background_image, [0,0])
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])
# 7repeat 6 over and over over
	pygame.display.flip()