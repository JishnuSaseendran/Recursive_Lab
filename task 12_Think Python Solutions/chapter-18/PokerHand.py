
from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        for rank, count in self.ranks.items():
            if count > 1:
                return True
        return False

    def has_twopair(self):
        self.rank_hist()
        pair_count = 0
        for count in self.ranks.values():
            if pair_count >1:
                return True
            if count > 1:
                pair_count += 1
        return False

    def has_three_of_a_kind(self):
        self.suit_hist()
        for val in self.suits.values():
            if val == 3:
                return True
        return False


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print
        print "Hand has flush", hand.has_flush()
        print "Hand has pair", hand.has_pair()
        print "Has has at least two pair", hand.has_twopair()
        print "Hand has 3 of a kind", hand.has_three_of_a_kind()
        print "#" * 40
