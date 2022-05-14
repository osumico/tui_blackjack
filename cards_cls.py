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
    
    @abstractmethod
    def draw(self) -> None:
        pass
    
    @abstractmethod
    def hide(self) -> None:
        pass
    
    @abstractmethod
    def show(self) -> None:
        pass
    

class Card(ICard):
    '''
The base class of a playing card. The functionality is implemented in methods:

- price: set the self.points of the card
- show/hide: show front/back of card
- draw: draws the map, should called when the class is initialized.
    '''
    points = int()
    val_suit = {
        'value': str(),
        'suit': str(),
    }
    card_draw = {
        'front': str(),
        'back': str(),
    }
    
    back_fillers = [
        '+',
        '#',
        '.',
    ]
    
    front_filler = [
        ' ',
        '.',
    ]
    
    def __init__(self, suit: str, value: str) -> None:
        
        self.val_suit['suit'] = suit
        self.val_suit['value'] = value
        self.price()
      
    
    def price(self) -> None:
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
     
     
    def ace_price(self, ace_choce: int = 0) -> None:
        match ace_choce:
            case 0:
                self.points = 1
            case 1:
                self.points = 11
    
    
    def draw(self, bfiller: str = back_fillers[1], ffiller: str = front_filler[0]) -> None:
        card_front = \
f""" _____
|{self.val_suit['value'].ljust(2, ffiller)}{ffiller * 3}|
|{ffiller * 2}{self.val_suit['suit']}{ffiller * 2}|
|{ffiller * 3}{self.val_suit['value'].rjust(2, ffiller)}|
 ‾‾‾‾‾"""
        card_back = \
f""" _____
|{bfiller * 5}|
|{bfiller * 5}|
|{bfiller * 5}|
 ‾‾‾‾‾"""
 
        self.card_draw['front'] = card_front
        self.card_draw['back'] = card_back
        
        
    def hide(self) -> str:
        return self.card_draw['back']
    
    def show(self) -> str:
        return self.card_draw['front']
    
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
    def draw_card(self) -> object:
        pass
    
    

class Deck(IDeck):

    suit_types = list()
    card_deck = list()
    all_types = list()
    
    small_types = [str(cardt) for cardt in range(2, 10 + 1)]
    big_types = [str(cardt) for cardt in "JQKA"]

    def __init__(self, suit: str = "V^*o") -> None:
        self.suit_types = [str(cardt) for cardt in "V^*o"]
        self.all_types = self.small_types + self.big_types
        
        for suit in self.suit_types:
            for types in self.all_types:
                self.card_deck.append((suit, types))
                
    def shuffle(self) -> None:
        random.shuffle(self.card_deck)
        
    def draw_card(self) -> tuple:
        return self.card_deck.pop()