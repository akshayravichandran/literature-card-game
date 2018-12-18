from game import Game
from card import Card
from constants import DeckType, Suit, HalfSuit, FaceValue
import pygame  

# Test Game Loop
def main():

        g = Game(players_per_team=2)

        # Dimensions
        x = 50
        y = 50
        width = 100
        height = 100
        win = pygame.display.set_mode((500,500))

        pygame.init()

        # hardcoding player1 to start
        g.current_player = g.team_1.players[0]
        #print(g.team_2.players[0].cards)

        # simulation constants
        flag = 1
        cardToAsk_1 = Card(FaceValue.SIX, Suit.CLUB, HalfSuit.LOWER)         
        cardToAsk_2 = Card(FaceValue.FIVE, Suit.CLUB, HalfSuit.LOWER)         

        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:    #any type of key press
                    if event.key == pygame.K_SPACE:
                        g.pick_random_starting_player()

            # Ask action (assume player chose to ask)

            playerToAsk = g.team_2.players[0]

            # Different card each loop - simulate user input
            if flag==1:
                cardToAsk = cardToAsk_1
                flag+=1
            else:
                cardToAsk = cardToAsk_2

            # get the actual card reference from the deck
            cardToAsk = g.deck.get_card_object(cardToAsk)
            
            if playerToAsk.has_card(cardToAsk):
                playerToAsk.remove_card(cardToAsk)
                g.current_player.add_card(cardToAsk)
                print(repr(g.current_player)+" collected "+ repr(cardToAsk) + " from " + repr(playerToAsk))
            else:
                g.current_player = playerToAsk
                print("Turn move to " + repr(playerToAsk))
                break


            #pygame.draw.rect(win, (0,255,0), (x,y,width,height))
            #pygame.display.update()

        pygame.quit()     # Once we leave the loop, close the window.


main()