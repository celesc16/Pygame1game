import pygame
from components import consts

class Player():
    def __init__(self , x , y , image):
        self.image = image
        self.shape = pygame.Rect( 0 , 0 , consts.HEIGHT_PLAYER , consts.WIDHT_PLAYER)
        self.shape.center = (x,y)
    
    def motion(self, delta_x , delta_y): 
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

    def drow(self, interface):
        interface.blit(self.image, self.shape )
        # pygame.draw.rect(interface , consts.COLOR_PLAYER , self.shape , width=1)