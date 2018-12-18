class Player:
    def __init__(self, player_id, name='', cards={}):
        self.player_id = player_id
        self.name = name
        self.cards = set(cards)

    def has_cards(self):
        return len(self.cards) == 0

    def add_card(self, card):
        self.cards.add(card)

    def has_card(self, card):
        if card in self.cards:
            return True
        return False

    def has_set(self, card):
        for c in self.cards:
            if c.suit == card.suit and c.half_suit == card.half_suit:
                return True
        return False

    def remove_card(self, card):
        self.cards.remove(card)

    def __repr__(self):
        return self.name
