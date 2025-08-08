import random
from circleshape import *
from constants import *


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius) #LN2

        random_angle = random.uniform(20,50)

    def draw(self,screen):
        pygame.draw.circle(screen,(204,102,0),self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            self.split_spawn()

           
    def split_spawn(self):
        random_angle = random.uniform(20,50)
        new_radii = self.radius - ASTEROID_MIN_RADIUS

        split_spawn1 = Asteroid(self.position.x,self.position.y,new_radii)
        split_spawn1.velocity = 1.2 *self.velocity.copy().rotate(random_angle) #LN4
        
        split_spawn2 = Asteroid(self.position.x,self.position.y,new_radii)
        split_spawn2.velocity = 1.2 * self.velocity.copy().rotate(-random_angle)
        


        



