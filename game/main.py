import pygame , sys
from components import consts
from entities import player

class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.window = pygame.display.set_mode((consts.WINDOW_WIDHT, consts.WINDOW_HEIGHT))
        # Check frame rate
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Adventures Games")  # Modificar nombre de juego después

        mainPlayer_image = pygame.image.load("assets//image//characters//mainPlayer//idle//HeavyBandit_Idle_0.png")

        self.mainPlayer = player.Player(50, 50, mainPlayer_image)

        # Definition of var for movement of player
        self.isJump = False
        self.jumpCount = 0

        self.left = False
        self.right = False
        self.isDown = False

    def run(self):
        # Bucle para cuando se abra la ventana y se cierre cuando presione lo correspondiente
        while True:
            # FPS control
            self.clock.tick(consts.FPS)

            self.window.fill(consts.COLOR_BG)

            # Calc de movement of player
            delta_x = 0
            delta_y = 0

            if self.right:
                delta_x = consts.SPEED

            if self.left:
                delta_x = -consts.SPEED

            if self.isJump:
                delta_y = -consts.SPEED

            if self.isDown:
                delta_y = consts.SPEED

            # Input motion
            self.mainPlayer.motion(delta_x, delta_y)

            self.mainPlayer.drow(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Cierra el programa completamente

                # Recognize when a key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.left = True

                    if event.key == pygame.K_d:
                        self.right = True

                    if event.key == pygame.K_w:
                        self.isJump = True

                    if event.key == pygame.K_s:
                        self.isDown = True

                # When the key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.left = False

                    if event.key == pygame.K_d:
                        self.right = False

                    if event.key == pygame.K_w:
                        self.isJump = False

                    if event.key == pygame.K_s:
                        self.isDown = False

            # Refresh window
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
