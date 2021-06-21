import numpy as np

#Set base variables for the deck of cards
suits = ['c', 'd', 'h', 's']
types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
face_cards = ['J', 'Q', 'K', 'A']
deck = []
players = []
board = []

#Add all the standard playing cards to the deck
for t in types:
    for s in suits:
        deck.append(t + s)

def add_player(name):
    name = []
    players.append(name)
    return name

def give_card(player):
    card = np.random.choice(deck, size=1, replace=False)
    player.append(card[0])
    deck.remove(card)

def burn_card():
    card = np.random.choice(deck, size=1, replace=False)
    deck.remove(card)

def deal_starting_cards(num_cards):
    while num_cards > 0:
        for p in players:
            give_card(p)
        num_cards -= 1

def deal_community_cards(num_cards):
    burn_card()
    while num_cards > 0:
        give_card(board)
        num_cards -= 1

def deal_flop():
    deal_community_cards(3)

def deal_turn():
    deal_community_cards(1)

def deal_river():
    deal_community_cards(1)

def check_total(player):
    total = 0
    aces = 0
    for card in player:
        value = card[0]
        if value in face_cards:
            if value != 'A':
                total += 10
            else:
                aces += 1
                total += 11
        else:
            total += int(value)
            if value == '1':
                total += 9
    if total == 21:
        return [total]
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    if aces > 0:
        return [total, total - 10]
    return [total]

def display_total(player):
    total = check_total(player)
    if len(total) > 1:
        print(str(total[0]) + "/" + str(total[1]))
    else:
        print(total[0])

