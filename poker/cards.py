import random

class Card:
    # card class
    def __init__(self, rank, suit):

        if rank not in [
            '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'A', 'J', 'Q', 'K']:
                raise ValueError("Invalid rank")

        valid_suits = ['D', 'S', 'C', 'H']
        if suit not in valid_suits:
            raise ValueError(f"Invalid suit. Valid suits are {valid_suits}")


        self.suit = suit
        self.rank = rank
        self.value = 0
        
        if self.rank.isnumeric():
            self.value = int(self.rank)
        elif self.rank == 'J':
            self.value = 11
        elif self.rank == 'Q':
            self.value = 12
        elif self.rank == 'K':
            self.value = 13
        elif self.rank == 'A':
            self.value = 14

    # unicode value to print suit symbols
    suit_lu = {
        "C": "\u2663",
        "H": "\u2665",
        "D": "\u2666",
        "S": "\u2660"
    }    
    
    def __repr__(self):
        rep = f"Card('{self.rank}', '{self.suit}')"
        return rep

    def __str__(self):
        string = "".join((str(self.rank), self.suit_lu[self.suit]))
        return string
       
       

class Deck():
    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.shuffle()

    def fill_deck(self):
        suits = ["C", "D", "S", "H"]    
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(r, s) for r in ranks for s in suits]
        
    def clear_deck(self):
        self.cards = []

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal(self, num_cards = 1):
        # TODO test
        return([self.cards.pop(0) for _ in range(num_cards)])

    def __str__(self):
        num_remaining = f"Cards Remaining: {len(self.cards)}"
        next_card =  f"Next Card: {str(self.cards[0])}"  
        return num_remaining + '\n' + next_card

    def __repr__(self):
        return f'Deck({self.cards})'
