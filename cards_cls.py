from abc import ABCMeta, abstractmethod
import random


class ICard:
    '''
A metaclass whose task is to implement a convenient interface for accessing maps, i.e.
successor classes. 
    '''
    
    __metaclass__ = ABCMeta
    
        
    @abstractmethod
    def __init__( self, suit: str, value: str) -> None:
        
        pass
    
    
    @abstractmethod
    def price(self) -> int:
        pass


class Card(ICard):
    '''
The base class of a playing card. The functionality is implemented in methods:

- price: set the self.points of the card called when the class is initialized.
- ace_price: set price card if this ace, need call ace_check() before this
    '''
    
    
    def __init__(self, suit: str, value: str) -> None:
        self.points = 0
        self.val_suit = {
            'value': value,
            'suit': suit,
        }
        self.card_draw = {
            'front': str(),
            'back': str(),
        }
        self.price()
      
    
    def price(self) -> None:
        '''
Call self.points if you need price of card. That method only set price of card.
        '''
        
        value = self.val_suit['value']
        
        try:
            self.points = int(value)
            
        except ValueError:
            
            if value in "JQK":
                self.points = 10
            else:
                self.points = 0 # WARN THIS IF ACE PRICE -- 0!
        
                
    @staticmethod
    def ace_check(value: str) -> bool:
        if value == "A":
            return True
        
        return False
     
    
    def value(self) -> str:
        return self.val_suit['value']
    
    
    def suit(self) -> str:
        return self.val_suit['suit']
    
    
class IDeck():
    '''
Metaclass that defines the interface semblance for the future deck of cards object (i.e. the successor of this metaclass)
    '''
    
    __metaclass__ = ABCMeta

    
    @abstractmethod
    def __init__(self) -> None:
        pass

    
    @abstractmethod
    def shuffle(self) -> None:
        pass


    @abstractmethod
    def draw_card(self) -> tuple:
        pass
    

class Deck(IDeck):
    '''
The base class of a deck of cards, provides the creation of a new deck, and drawing cards from the deck with subsequent removal in the current deck object. The functionality is implemented in the methods:

- shuffle: shuffle the deck, returns nothing
- draw_card: draw the last card, remove it from the deck. Returns a tuple.
    '''

    
    suit_types = list()
    all_types = list()    
    small_types = [str(cardt) for cardt in range(2, 10 + 1)]
    big_types = [str(cardt) for cardt in "JQKA"]


    def __init__(self, suit: str = "♠♥♦♣") -> None:
        self.card_deck = list()
        self.suit_types = [str(cardt) for cardt in suit]
        self.all_types = self.small_types + self.big_types
        
        for suit in self.suit_types:
            for types in self.all_types:
                self.card_deck.append((suit, types))
                
                
    def shuffle(self) -> None:
        random.shuffle(self.card_deck)

        
    def draw_card(self) -> tuple:
        return self.card_deck.pop()
