import pygame , sys
import settings
from levels.level import Level

class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDHT, settings.SCREEN_HEIGHT))
        
        pygame.display.set_caption("Adventures Games")  # Modificar nombre de juego después
        # Check frame rate                      
        self.clock = pygame.time.Clock()  

        self.level = Level()                                                              

    def run(self):
        # Bucle para cuando se abra la ventana y se cierre cuando presione lo correspondiente
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Cierra el programa completamente

            # Refresh screen
            self.clock.tick(settings.FPS)
            self.screen.fill(settings.COLOR_BG)
            self.level.run()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
