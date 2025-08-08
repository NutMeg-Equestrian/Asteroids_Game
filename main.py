import pygame
import sys
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock() #pygame.time.Clock() is a class and needs to be assigned to a variable name to create an object
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Declared as None so nonlocal will work properly
    player = None
    asteroids = None
    shots = None
    updatable = None
    drawable = None
    asteroid_field = None

    def game_state_reset():
        nonlocal player, asteroids, shots, updatable, drawable, asteroid_field
    
        #Groups first
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        #Then set containers
        Asteroid.containers = (asteroids, updatable, drawable)
        Player.containers = (updatable, drawable)
        AsteroidField.containers = (updatable,)
        Shot.containers = (shots, updatable, drawable)
    
        #Finally create objects
        player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        asteroid_field = AsteroidField()
        #shot = Shot(player.position.x,player.position.y) LN3
    
    game_state_reset()
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                game_state_reset()
                game_over = False
                

        
        dt = clock.tick(60)/1000 #we call the tick method on clock (our time/clock object) the 60 pauses the loop until 1/60th of a second has passed since the last loop
        screen.fill("black")
        if not game_over:

            for sprite in updatable:
                sprite.update(dt)

            for asteroid in asteroids:
                if player.collision_happens(asteroid):
                    game_over = True
                    
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collision_happens(asteroid):
                        shot.kill()
                        asteroid.split()

            for sprite in drawable:
                sprite.draw(screen)
        else:
            font_end = pygame.font.Font(None,74)
            font_instr = pygame.font.Font(None,45)
            text = font_end.render("GAME OVER", True,(255,255,0))
            rect = text.get_rect(center=screen.get_rect().center)
            screen.blit(text,rect)
            instr = font_instr.render("Press \"y\" key to restart", True, (255, 255, 255))
            rect2 = instr.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 80))
            screen.blit(instr, rect2)


        pygame.display.flip()
        

if __name__ == "__main__":
    main()
