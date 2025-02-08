
#from poker import cards
import cards
from collections import Counter

class Hand:
    def __init__(self):
        self.cards = []

    def show(self):
        print(f'hand: {", ".join(str(card) for card in self.cards)}')

    def has_high_card_only(self):
        
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())
        hand_has_high_card_only = unique_counts.count(1) == 5
        return hand_has_high_card_only  

    def has_pair(self):
        
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())
        hand_has_pair = unique_counts.count(2) > 0

        result = (
            hand_has_pair and 
            not self.has_two_pair() and
            not self.has_three_of_kind() and
            not self.has_four_of_kind() and
            not self.has_full_house()
        )
        return result     

    def has_two_pair(self):
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())
        hand_has_two_pair = unique_counts.count(2) == 2   

        result = (
            hand_has_two_pair and 
            not self.has_four_of_kind()
        )
        return result      

    def has_three_of_kind(self):
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())
        hand_has_three_of_kind = unique_counts.count(3) == 1  

        result = (
            hand_has_three_of_kind and
            not self.has_full_house()
        )
        return result      

    def has_four_of_kind(self):
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())
        return unique_counts.count(4) == 1  

    def has_full_house(self):
        ranks = [card.rank for card in self.cards]
        unique_counts = list(Counter(ranks).values())

        result = (
            unique_counts.count(3) == 1 and 
            unique_counts.count(2) == 1 
        )
        return result

    def has_flush(self):

        suits = [card.suit for card in self.cards]
        unique_counts = list(Counter(suits).values())
        hand_has_flush = unique_counts.count(5) == 1 
        
        result = (
            hand_has_flush and 
            not self.has_straight_flush()
        )
        return result

    def has_straight(self):
        values = [card.value for card in self.cards]
        possible = max(values) - min(values) == 4

        result = (
            possible and
            not self.has_pair() and
            not self.has_two_pair() and
            not self.has_three_of_kind() and
            not self.has_four_of_kind() and
            not self.has_flush() and 
            not self.has_straight_flush()
        )
        return(result)

    def has_straight_flush(self):

        suits = [card.suit for card in self.cards]
        unique_counts = list(Counter(suits).values())
        values = [card.value for card in self.cards]

        result = (
            (max(values) - min(values) == 4) and
            unique_counts.count(5) == 1
        )            
        return result
       

    def assign_hand_value(self):
        
        self.value = (

            (
                self.has_high_card_only() * 1 + 
                self.has_high_card_only() * self.get_rank_value() + 
                self.has_high_card_only() * self.get_kicker_value()
            ) + (
                self.has_pair() * 100 + 
                self.has_pair() * self.get_rank_value() + 
                self.has_pair() * self.get_kicker_value()
            ) + (
                self.has_two_pair() * 200 + 
                self.has_two_pair() * self.get_rank_value() +
                self.has_two_pair() * self.get_kicker_value()
            ) + (
                self.has_three_of_kind() * 300 + 
                self.has_three_of_kind() * self.get_rank_value() +
                self.has_three_of_kind() * self.get_kicker_value()
            ) + (
                self.has_straight() * 400 + 
                self.has_straight() * self.get_rank_value() +
                self.has_straight() * self.get_kicker_value()
            ) + (
                self.has_flush() * 500 + 
                self.has_flush() * self.get_rank_value() +
                self.has_flush() * self.get_kicker_value()
            ) + (
                self.has_full_house() * 600 + 
                self.has_full_house() * self.get_rank_value() +
                self.has_full_house() * self.get_kicker_value()
            ) + (
                self.has_four_of_kind() * 700 + 
                self.has_four_of_kind() * self.get_rank_value() +
                self.has_four_of_kind() * self.get_kicker_value()
            ) + (
                self.has_straight_flush() * 800 + 
                self.has_straight_flush() * self.get_rank_value() +
                self.has_straight_flush() * self.get_kicker_value()
            )
        )

    def get_rank_value(self):

        if self.has_high_card_only():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 1}
            rank_value = max(filtered_counts.keys())

        if self.has_pair():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 2}
            rank_value = max(filtered_counts.keys())

        if self.has_two_pair():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 2}
            rank_value = max(filtered_counts.keys())

        if self.has_three_of_kind():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 3}
            rank_value = max(filtered_counts.keys())

        if self.has_straight():
            values = [card.value for card in self.cards]
            rank_value = max(values)    

        if self.has_flush():
            values = [card.value for card in self.cards]
            rank_value = max(values)  

        if self.has_full_house():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 3}
            rank_value = max(filtered_counts.keys())

        if self.has_four_of_kind():
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 4}
            rank_value = max(filtered_counts.keys())

        if self.has_straight_flush():
            values = [card.value for card in self.cards]
            rank_value = max(values)  
            
        return rank_value


    def get_kicker_value(self):

        if self.has_high_card_only():
            # 4 orders of kicker which are the ranks of the cards that is not the high card
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 1}
            filtered_counts = list(filtered_counts)
            filtered_counts.sort(reverse = True)
            kicker = filtered_counts[1] /100 + filtered_counts[2] /1000 + \
            filtered_counts[3] /10000 + filtered_counts[4] /10000

        if self.has_pair():
            # three orders of kicker which are the ranks of the cards not involved in the pair
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 1}
            filtered_counts = list(filtered_counts)
            filtered_counts.sort(reverse = True)
            kicker = filtered_counts[0] /100 + filtered_counts[1] /1000 + filtered_counts[2] /10000

        if self.has_two_pair():
            # first order kicker is the lowest pair value (highest is rank)  
            # second order is unpaired card value
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts1 = {k: v for k, v in counts.items() if v == 1} # other card
            filtered_counts2 = {k: v for k, v in counts.items() if v == 2} # the pairs
            filtered_counts1 = list(filtered_counts1) 
            filtered_counts2 = list(filtered_counts2)
            kicker = filtered_counts1[0] /100 + min(filtered_counts2) / 1000

        if self.has_three_of_kind():
            # kicker - 2 orders. The rank of the cards not involved in the triplet
            values = [card.value for card in self.cards]
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v != 3}
            kicker = max(filtered_counts.keys()) / 100  + min(filtered_counts.keys()) / 1000

        if self.has_flush():
            # kicker - 4 orders. The rank of the cards that are not the hand rank
            values = [card.value for card in self.cards]
            values.sort(reverse = True)
            kicker = values[1] / 100 + values[2] /1000 + \
                values[3] /10000 + values[4] / 100000   

        if self.has_full_house():
            # kicker is the rank of the pair
            values = [card.value for card in self.cards]            
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 2}
            kicker = max(filtered_counts.keys())

        if self.has_four_of_kind():
            # no kicker
            values = [card.value for card in self.cards]  
            counts = Counter(values)
            filtered_counts = {k: v for k, v in counts.items() if v == 1}
            kicker = min(filtered_counts.keys())

        if self.has_straight() or self.has_straight_flush():
            # no kicker
            kicker = 0

        return kicker 

class Player:
    def __init__(self, purse = 0):
        self.purse = 0
        self.hand = Hand()

    def credit(self, amount):
        self.purse = self.purse + amount

    def debit(self, amount):
        self.purse = self.purse - amount



class Table:

    def __init__(self, num_players = 2):
        # TODO max players 8
        self.deck = cards.Deck()
        self.players = [Player(100) for _ in range(0, num_players)]
        for p in self.players:
            p.hand.cards = self.deck.deal(5)
            p.hand.assign_hand_value()


   
table = Table()
table.players
table.players[0].hand.show()
table.players[1].hand.show()
print(table.players[0].hand.value)
print(table.players[1].hand.value)



hand1 = Hand()

hand1.cards = [
    cards.Card('7', 'D'), 
    cards.Card('7', 'C'), 
    cards.Card('2', 'S'), 
    cards.Card('2', 'D'),
    cards.Card('Q', 'C')
]
hand1.assign_hand_value()
hand1.hand_value

table.players[0].purse



table.deck

player1 = Player()

deck = Deck()

hand1 = Hand() 
hand1.cards = deck.deal(5)

hand2 = Hand() 
hand2.cards = deck.deal(5)

hand1.assign_hand_value()
hand2.assign_hand_value()

hand1.show()
hand2.show()
hand1.hand_value
hand2.hand_value





hand2 = Hand() 
hand2.cards = [
    cards.Card('7', 'D'), 
    cards.Card('8', 'D'), 
    cards.Card('2', 'C'), 
    cards.Card('Q', 'D'),
    cards.Card('6', 'D')
]
hand1.assign_hand_value()
hand2.assign_hand_value()
hand1.hand_value > hand2.hand_value
hand2.hand_value > hand1.hand_value

hand2.hand_value

table = Table()
table.hands = [hand1, hand2]

for hand in table.hands:
    hand.assign_hand_value()

table.hands[0].hand_value
table.hands[1].hand_value

[hand.hand_value for hand in table.hands]

[hand.assign_hand_value() for hand in table.hands]



hand.assign_hand_value()
hand.hand_value


hand.has_pair()
hand.has_two_pair()
hand.has_three_of_kind()
hand.has_full_house()
hand.has_four_of_kind()
hand.has_flush()
hand.has_straight()
hand.has_straight_flush()



