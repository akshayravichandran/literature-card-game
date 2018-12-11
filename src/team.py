class Team:
    def __init__(self, team_id, players=[]):
        self.team_id = team_id
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def has_cards(self):
        for player in self.players:
            if player.has_cards():
                return True
        return False

    def __str__(self):
        return "Team: " + str(self.team_id) +"\nPlayers: " + str(self.players)
