import pygame
    
Display = pygame.display.set_mode((400,700)) 

class Draw():                                       # Class Pygame Draw Button
    
    def __init__ (self,color,x,y,widht,height):     # Set Variable
        self.color = color
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
    def set_color (self,color):                     # Set Color
        self.color = color
        return self.Rect()
    
    def Rect (self):                                # Draw Rect
        return pygame.draw.rect(Display,self.color,(self.x,self.y,self.widht,self.height))
    
    def Circle(self):                               # Draw Circle
        return pygame.draw.circle(Display,self.color,(self.x+self.widht)/2,(self.y+self.height)/2,)
    
    def isPosition(self,pos):                       # Check Position Mouse
        if pos[0] > self.x and pos[0] < self.x + self.widht :
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

