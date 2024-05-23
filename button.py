import pygame
from constants import *

class Button(object):
    def __init__(self,x,y,width,height,text,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.Font(None,40)
        self.text = self.font.render(text,True,WHITE)
        self.bg_color = color

    def draw(self,screen):
        
        pygame.draw.rect(screen,self.bg_color,self.rect)
        
        width = self.text.get_width()
        height = self.text.get_height()
        
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        
        screen.blit(self.text,(posX,posY))

    def isPressed(self):

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
            
    def change_bg_color(self,color):
        self.bg_color = color