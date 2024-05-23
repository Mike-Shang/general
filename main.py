import pygame
from constants import *
from calculator import Calculator


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Calculator")

    done = False

    clock = pygame.time.Clock()

    calculator = Calculator()

    while not done:
        
        done = calculator.process_events()
        
        calculator.run_logic()
        
        calculator.display_frame(screen)
    
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
