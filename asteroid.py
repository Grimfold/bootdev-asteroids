import circleshape, pygame, random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y, self.radius)
 
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(0 - random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vec1 * 1.2
        a2.velocity = vec2 * 1.2


        