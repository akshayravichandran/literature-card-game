from constants import PlayerActions
from constants import DeckType
from deck import Deck
from player import Player
from team import Team
import random


class Game:
    def __init__(self, players_per_team=3, deck_type=DeckType.STANDARD):
        self.team_1 = Team(1)
        self.team_2 = Team(2)
        self.players_per_team = players_per_team
        self.deck_type = deck_type
        self.current_player = None

        # Initialize players in teams
        for i in range(1, players_per_team+1):
            self.team_1.add_player(Player(i, "player"+str(i)))
        for i in range(players_per_team+1, 2*players_per_team+1):
            self.team_2.add_player(Player(i, "player"+str(i)))

        self.deal_cards()
        self.pick_random_starting_player()

    # Deal cards to all players
    def deal_cards(self):
        deck = Deck(self.deck_type)
        deck.shuffle()
        players = self.team_1.players + self.team_2.players
        player_index = 0
        for card in deck.cards:
            players[player_index].add_card(card)
            player_index = (player_index + 1) % len(players)

    # COULD HONESTLY BE IN CONSTRUCTOR. USED ONLY ONCE
    # Select random starting player
    def pick_random_starting_player(self):
        self.current_player = random.choice(self.team_1.players + self.team_2.players)

    # CLI Interface. Presents available actions to the current player and asks him to choose.
    def read_action(self):
        allowed_actions = []
        if self.current_player.has_cards:
            allowed_actions.append(PlayerActions.DECLARE)
            if self.get_current_player_opponent_team().has_cards:
                allowed_actions.append(PlayerActions.ASK)
        else:
            if self.get_current_player_team().has_cards:
                allowed_actions.append(PlayerActions.PICK_TEAMMATE)
            elif self.get_current_player_opponent_team().has_cards():
                allowed_actions.append(PlayerActions.PICK_OPPONENT)
            else:
                return False

        # Print player cards
        # Print allowed actions
        # Get input
        # Return input

    # Return the current player's team
    def get_current_player_team(self):
        return self.team_1 if self.current_player in self.team_1 else self.team_2

    # Return the opposing team player's team
    def get_current_player_opponent_team(self):
        return self.team_1 if self.current_player in self.team_2 else self.team_1

    # Display current state of game
    def show_game(self):
        print("Current player: "+repr(self.current_player))
