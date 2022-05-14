from abc import ABCMeta, abstractmethod
import cards_cls as C

class IPlayer:
    '''
Metaclass defining a player, player is an abstraction, the current player is defined by a special variable.
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def to_hand(self) -> None:
        pass

    @abstractmethod
    def price(self) -> dict:
        pass

    @abstractmethod
    def extract_stat(self) -> dict:
        pass
    
class Player(IPlayer):
    
    range_check = 0
    aces_count = 0
    pstat = {
        'prices': 0,
        'money': int(),
        'hand_card': list(),
    }
    
    def __init__(self, smoney: int) -> None:
        self.pstat['money'] = smoney
    
    def to_hand(self, card: tuple) -> None:
        
        if card not in self.pstat['hand_card']:
            self.pstat['hand_card'].append(card)
            
        self.price()
    
    def price(self) -> None:
        
        hand = self.pstat
        for i in range(self.range_check, len(hand['hand_card'])):
            
            suit = hand['hand_card'][i][0]
            value = hand['hand_card'][i][1]
            card = C.Card(suit, value)
            
            if card.ace_check(value):
                self.aces_count += 1
                
            self.pstat['prices'] += card.points
        self.range_check += 1
    
    def extract_stat(self) -> dict:
        return self.pstat