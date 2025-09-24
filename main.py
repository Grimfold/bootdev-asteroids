import pygame, sys
import player, asteroid, asteroidfield, shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    asteroid.Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = updatables

    shot.Shot.containers = (shots, updatables, drawables)

    a = asteroidfield.AsteroidField()

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

        # Check for Collisions
        for roid in asteroids:
            if p.collision(roid):
                print("Game Over!")
                sys.exit()
            for ammo in shots:
                if roid.collision(ammo):
                    ammo.kill()
                    roid.split()

        # Draw drawables
        for drawable in drawables:
            drawable.draw(screen)

        # Update Display
        pygame.display.flip()

        # Max 60 fps
        dt = ( clock.tick(60) / 1000 )

if __name__ == "__main__":
    main()
