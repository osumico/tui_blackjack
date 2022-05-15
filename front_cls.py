from abc import abstractmethod


class Drawer:
    '''
A class that draws playing cards, and the cards in the player's hand. The functionality of the class is implemented in the method:

- form_vhand: returns a string with cards arranged in a row, the second parameter determines the visibility of the cards.
    '''
    
    back_fillers = [
        '+',
        '#',
        '.',
    ]
    front_filler = [
        ' ',
        '.',
    ]
    
    def __init__(self, card_valsuit: tuple) -> None:
        
        self.card_draw = {
            'front': str(),
            'back': str(),
        }
        
        self.val_suit = {
            'suit': card_valsuit[0],
            'value': card_valsuit[1],
        }
        
        self.draw()
    
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
    
    @staticmethod
    def form_vlist(hand: list, is_show: bool) -> list:
        
        dhand = list()
        for card in hand:
            dcard = Drawer(card)
            
            if is_show:
                dhand.append(dcard.show())
                
            else:
                 dhand.append(dcard.hide())
            
        return dhand

    @staticmethod
    def form_vhand(hand: list, is_show: bool) -> list:
        
        hand_drawc = Drawer.form_vlist(hand, is_show)
        card_string, lines = '', 0
        
        for i in range(len(hand_drawc[0])):
            for card in hand_drawc:
                card = card.splitlines()
                try:
                    card_string += f"{card[i]}\t"
                except:
                    pass
                
            if lines != (len(card[0]) - 2):
                card_string += "\n"
                lines += 1
                
        return card_string

    def hide(self) -> str:
        return self.card_draw['back']
    
    def show(self) -> str:
        return self.card_draw['front']
    
    
class TUI:
    pass