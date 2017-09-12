import pygame

pygame.init()

display_width = 512
display_height = 480




screenSize = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Game On!!')

clock = pygame.time.Clock()


hero_image = pygame.image.load('images/hero.png')

def hero(x,y):
	screenSize.blit(hero_image, (x,y))

x = (display_width * 0.2)
y = (display_height * 0.3)


	


game_on = False

while not game_on:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = True

		

	



	hero(x,y)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
quit()	