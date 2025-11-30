import pygame

pygame.init()

pygame.display.set_mode((500,500))

done = False

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
      

    pygame.display.flip()