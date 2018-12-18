from game import Game
from card import Card
from constants import DeckType, Suit, HalfSuit, FaceValue
import pygame 
import time

# Test Game Loop
def main():

        g = Game(players_per_team=2)

        #Dimensions
        x = 50
        y = 50
        width = 100
        height = 100
        win = pygame.display.set_mode((500,500))

        pygame.init()

        # hardcoding player1 to start
        g.current_player = g.team_1.players[0]

        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:    #any type of key press
                    if event.key == pygame.K_SPACE:
                        g.pick_random_starting_player()

            # get action to perform
            action = input("Ask or Declare? ")
            if(action == "ask"):

                # get player to ask from 
                player_num = int(input("Enter player number "))
                player_to_ask = g.get_player_from_num(player_num)
                print(repr(player_to_ask))

                # make sure you ask from other team only
                if(g.check_if_players_on_same_team(g.current_player, player_to_ask)):
                    print("Error: Players on same team")
                    continue
                else:
                    print("Asking "+repr(player_to_ask))

                # get card to ask
                (fv, s, ls) = input("Enter Card FaceValue, Suit, HalfSuit: ").split(',')
                card_to_ask = Card(FaceValue[fv], Suit[s], HalfSuit[ls])

                # get the actual card reference from the deck
                card_to_ask = g.deck.get_card_object(card_to_ask)
                
                # if currentplayer can ask for the card:
                if g.current_player.has_set(card_to_ask):
                    if player_to_ask.has_card(card_to_ask): 
                        player_to_ask.remove_card(card_to_ask)
                        g.current_player.add_card(card_to_ask)
                        print(repr(g.current_player)+" collected "+ repr(card_to_ask) + " from " + repr(player_to_ask))
                    else:
                        g.current_player = player_to_ask
                        print(repr(player_to_ask)+" did not have "+repr(card_to_ask))
                        print("Turn moves to " + repr(player_to_ask))
                else:
                    print(repr(g.current_player) +" does not have a card in that set ")

            #pygame.draw.rect(win, (0,255,0), (x,y,width,height))
            #pygame.display.update()

        pygame.quit()     # Once we leave the loop, close the window.


main()