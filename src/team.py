class Team:
    def __init__(self, team_id, players=None):
        self.team_id = team_id
        self.players = players or []

    def add_player(self, player):
        self.players.append(player)

    def has_cards(self):
        for player in self.players:
            if player.has_cards():
                return True
        return False

    def has_player(self, player):
        if player in self.players:
            return True
        return False

    def __str__(self):
        return "Team " + str(self.team_id) +"\n"+ str(len(self.players)) + " Players: " + str(self.players)
