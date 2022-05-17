from cards_cls import Deck
from player_cls import Player
from front_cls import Drawer, TUI
import os
import time

player = Player(100, True)
dealer = Player(100, False)

deck = Deck()
deck.shuffle()

for _ in range(2):
    player.to_hand(deck.draw_card())

for _ in range(2):
    dealer.to_hand(deck.draw_card())

bet = 30
player.money(bet, False)
dealer.money(bet, False)

player_stat = player.extract_stat()
dealer_stat = dealer.extract_stat()

player_dhand = Drawer.form_vhand(player_stat['hand_card'], player_stat['is_player'])
dealer_dhand = Drawer.form_vhand(dealer_stat['hand_card'], dealer_stat['is_player'])
init_msg = TUI.init_message()

print(init_msg)
time.sleep(1)
os.system('cls')


pl_money, dl_money = player_stat['money'], dealer_stat['money']
header_msg = TUI.form_header(bet, 0, pl_money, dl_money)

print(header_msg)

score_m, score_d = TUI.showed_score(player_stat), TUI.showed_score(dealer_stat)
body_msg = TUI.form_body(player_dhand, dealer_dhand, score_m, score_d)

print(body_msg)

menu_msg = TUI.form_menu()
menu_msg = input(menu_msg)