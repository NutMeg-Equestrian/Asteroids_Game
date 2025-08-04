import pygame
from constants import * 

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock() #pygame.time.Clock() is a class and needs to be assigned to a variable name to create an object
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)/1000 #we call the tick method on clock (our time/clock object) the 60 pauses the loop until 1/60th of a second has passed since the last loop

if __name__ == "__main__":
    main()
