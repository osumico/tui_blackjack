from abc import ABCMeta, abstractmethod
import cards_cls as C

class IPlayer:
    '''
Metaclass defining a player, player is an abstraction, the current player is defined by a special variable.
    '''
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def to_hand(self) -> None:
        pass
    
    @abstractmethod
    def show_hand(self) -> None:
        pass
    
    @abstractmethod
    def points(self) -> None:
        pass
    
    @abstractmethod
    def extract_stat(self) -> None:
        pass
    
class Player(IPlayer):
    pass