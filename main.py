import pygame

from constants import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock
    dt = 0

    # Game Loop
    while True:

        # Closing Window closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Black background
        screen.fill("black")

        # Update Display
        pygame.display.flip()

if __name__ == "__main__":
    main()
