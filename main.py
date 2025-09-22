import pygame
import player

from constants import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    player.Player.containers = (updatables, drawables)
    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game Loop
    while True:

        # Closing Window closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Black background
        screen.fill("black")

        # Update updatable positions
        updatables.update(dt)

        # Draw drawables
        for drawable in drawables:
            drawable.draw(screen)

        # Update Display
        pygame.display.flip()

        # Max 60 fps
        dt = ( clock.tick(60) / 1000 )

if __name__ == "__main__":
    main()
