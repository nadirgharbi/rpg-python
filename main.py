import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
SIZE_SCREEN = (WIDTH, HEIGHT)
FPS = 60
screen = pygame.display.set_mode(SIZE_SCREEN)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#2c3e50")
    
    pygame.display.flip()
    
    clock.tick(FPS)
    
pygame.quit()