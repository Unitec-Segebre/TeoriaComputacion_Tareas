import sys, pygame
from automata_node import node_state
pygame.init()

size = width, height = 1024, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)

nodes = []

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	if pygame.mouse.get_pressed()[0]:
		flag_new_node = 1;
		for node_to_move in nodes:
			if node_to_move.rect.collidepoint(pygame.mouse.get_pos()):
				node_to_move.rect.center = pygame.mouse.get_pos()
				flag_new_node = 0;
		if flag_new_node:
			nodes.append(node_state(pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), 50)))

	if pygame.mouse.get_pressed()[2]:
		print (len(nodes))

	screen.fill(black)
	for node_to_draw in nodes:
		node_to_draw.rect = pygame.draw.circle(screen, (255, 255, 255), node_to_draw.rect.center, 50)
	pygame.display.flip()
