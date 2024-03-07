import pygame
import pygame.gfxdraw

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Application")

# Game loop
x=0
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    x += 10
    y = int(0.001 * x ** 2)  # Calculate y-coordinate of the parabola
    pygame.gfxdraw.pixel(screen, x, y, (255, 255, 255))
    y=0

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()