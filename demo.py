from cardgamebase import *

p1 = add_player("p1")
p2 = add_player("p2")

deal_starting_cards(2)
print(p1)
print(p2)
deal_flop()
deal_turn()
deal_river()
print(board)
display_total(p1)
display_total(p2)