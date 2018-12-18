# sample game - testing loop, turn switching and card changing
# no user input, just hardcoding few steps

from game import Game
import pygame 

# Test Game Loop
def main():

    g = Game(players_per_team=2)

    # Dimensions
    x = 50
    y = 50
    width = 100
    height = 100
    win = pygame.display.set_mode((500, 500))

    pygame.init()

    gameExit = False
    while not gameExit:
        print(g.current_player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g.pick_random_starting_player()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

    pygame.quit()     # Once we leave the loop, close the window.


main()
