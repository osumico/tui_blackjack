from cards_cls import Deck
from player_cls import Player
from front_cls import Drawer, TUI
import os, time
import random

INIT_CARD = 2
bet, turn, start = 20, 0, True
cash = 0
minx, maxy = (4, 8)
pl0 = Player(random.randint(minx, maxy) * 100, True)
pl1 = Player(random.randint(minx, maxy) * 100, False)

while True:
    
    deck = Deck()
    deck.shuffle()
    
    if start:
        print(TUI.init_message())
        time.sleep(1)
        os.system("cls")
        
        for _ in range(INIT_CARD):
            pl0.to_hand(deck.draw_card())
            pl1.to_hand(deck.draw_card())
            
            
        start = False
        
    pl0_stat = pl0.extract_stat()
    pl1_stat = pl1.extract_stat()
    hnd_pl0 = Drawer.form_vhand(pl0_stat['hand_card'], True)
    hnd_pl1 = Drawer.form_vhand(pl1_stat['hand_card'], False)
    
    tui_head = TUI.form_header(bet, turn, pl0_stat['money'], pl1_stat['money'])
    tui_body = TUI.form_body(hnd_pl0, hnd_pl1, TUI.showed_score(pl0_stat), TUI.showed_score(pl1_stat))
    tui_menu = TUI.form_menu()
    
    print(
        tui_head,
        tui_body,
        sep='\n'
    )
    
    tui_menu = input(tui_menu) # For player
    exit = False
    
    match tui_menu.lower():
        case "t":
            cash += (pl0.money(bet, False) + pl1.money(bet, False))
            pl0.to_hand(deck.draw_card())
            
            if pl1_stat['prices'] <= 16 and bool(random.getrandbits(1)):
                pl1.to_hand(deck.draw_card())
            
        case "i":
            bet *= 2
            cash += (pl0.money(bet, False) + pl1.money(bet, False))
            pl0.to_hand(deck.draw_card())
            
            if pl1_stat['prices'] <= 16 and bool(random.getrandbits(1)):
                pl1.to_hand(deck.draw_card())
            
        
        case "p":
            while True:
                if pl1_stat['prices'] <= 16 and bool(random.getrandbits(1)):
                    pl1.to_hand(deck.draw_card())
                else:
                    break

            if pl0_stat['prices'] > pl1_stat['prices']:
                exit_msg = "WIN"
                pl0.money(cash, True)
                cash = 0
                exit = True
            
            elif pl0_stat['prices'] < pl1_stat['prices']:
                exit_msg = "LOSE"
                pl1.money(cash, True)
                cash = 0
                exit = True
                
            else:
                exit_msg = "PAT!"
                pl0.money(cash // 2, True)
                pl1.money(cash // 2, True)
                cash = 0
                exit = True
                
    if pl0_stat['prices'] > 21:
        exit_msg = "AUTOLOSE"
        pl0.money(cash, True)
        cash = 0
        exit = True
    
    if pl1_stat['prices'] > 21:
        exit_msg = "AUTOWIN"
        pl1.money(cash, True)
        cash = 0
        exit = True
        
    if exit:
        
        hnd_pl0 = Drawer.form_vhand(pl0_stat['hand_card'], True)
        hnd_pl1 = Drawer.form_vhand(pl1_stat['hand_card'], True)
        
        tui_head = TUI.form_header(bet, turn, pl0_stat['money'], pl1_stat['money'])
        tui_body = TUI.form_body(hnd_pl0, hnd_pl1, TUI.showed_score(pl0_stat, True), TUI.showed_score(pl1_stat, True))
        tui_menu = TUI.form_menu()
        
        os.system("cls")
        print(
            tui_head,
            tui_body,
            sep='\n'
        )
        
        time.sleep(2)
        os.system("cls")
        print(exit_msg)
        break