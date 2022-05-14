import cards_cls as C
import player_cls as P
import front_cls as UI


player = P.Player(100)
deck = C.Deck()
deck.shuffle()

for _ in range(2):
    player.to_hand(deck.draw_card())
    
player.money(30, False)
print(player.extract_stat())


dealer = P.Player(100)
for _ in range(2):
    dealer.to_hand(deck.draw_card())
    
dealer.money(30, False)
print(dealer.extract_stat())