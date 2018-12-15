from game import Game
import pygame 

# Test Game Loop
def main():
        g1 = Game()

        #Dimensions
        x = 50
        y = 50
        width = 100
        height = 100
        win = pygame.display.set_mode((500,500))

        pygame.init()

        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            pygame.draw.rect(win, (0,255,0), (x,y,width,height))
            pygame.display.update()

        pygame.quit()     # Once we leave the loop, close the window.


main()