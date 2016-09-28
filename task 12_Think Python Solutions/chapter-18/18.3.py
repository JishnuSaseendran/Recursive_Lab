import sys
import os
import random

class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', 
        '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort(cmp=Card.__cmp__)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_of_hands, cards_per_hand):
        for hand_count in range(num_of_hands):
            hand_name = 'hand_num' + str(hand_count)
            hand = Hand(hand_name)
            print
            print "Created hand called", hand_name
            for card_count in range(cards_per_hand):
                hand.add_card(self.pop_card())
            print "Hand has cards"
            print hand
            print "=" * 30

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def main():
    hot_deck = Deck()
    hot_deck.deal_hands(4, 7)


if __name__ == "__main__":
    main()
