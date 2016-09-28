
from random import shuffle

class Card(object):

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                            Card.suit_names[self.suit])
    
    def __repr__(self):
        return 'Card <{}, {}>'.format(self.rank_names[self.rank], self.suit_names[self.suit])
   
  
 
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank



class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]
        
    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])
    
    def __repr__(self):
        return "Deck <{}>".format(self.cards)
    
    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        shuffle(self.cards)
        return "deck has been shuffled."
    
    def sort(self):
        self.cards.sort()
        return "deck has been sorted."
    




deck = Deck()
deck.shuffle()
deck
deck.sort()
print(deck)
