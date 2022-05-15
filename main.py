import cards_cls as C
import player_cls as P
import front_cls as UI


player = P.Player(100)
dealer = P.Player(100)

deck = C.Deck()
deck.shuffle()

for _ in range(2):
    player.to_hand(deck.draw_card())

for _ in range(2):
    dealer.to_hand(deck.draw_card())
    
player.money(30, False)
dealer.money(30, False)

player_stat = player.extract_stat()
dealer_stat = dealer.extract_stat()

player_dhand = UI.CDrawer.form_vhand(player_stat['hand_card'], True)
dealer_dhand = UI.CDrawer.form_vhand(dealer_stat['hand_card'], False)

print(player_dhand)
print(dealer_dhand)