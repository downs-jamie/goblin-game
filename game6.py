import pygame
import random


display_width = 360
display_height = 480
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
	# sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2if(move2 == False):
		goblin['x'] -= 1
	if goblin['x'] > 480:
		goblin['x'] += 1
		move2 = True)




pygame.init()
pygame.mixer.init()
screenSize = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game On!!')
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
	
game_on = True
while not game_on:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

		
	all_sprites.update()

	screen.fill(BLACK)
	all_sprites.draw(screenSize)

	
if(move2 == False):
		goblin['x'] -= 1
	if goblin['x'] > 480:
		goblin['x'] += 1
		move2 = True


	pygame.display.flip()
	

pygame.quit()
quit()	