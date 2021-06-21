from cardgamebase import *
from texas_holdem_headsup_ai import *

p1 = add_player("p1")
p2 = add_player("p2")

deal_starting_cards(2)
print(p1)
print(p2)
print("P1's hand is " + strength(p1))
print("P2's hand is " + strength(p2))