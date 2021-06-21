from cardgamebase import *

def pocket_pair(player):
    if player[0][0] == player[1][0]:
        return True
    else:
        return False

def broadway(card):
    if card[0] in face_cards or card[0] == '1':
        return True
    else:
        return False

def two_broadway(player):
    if broadway(player[0]) and broadway(player[1]):
        return True
    else:
        return False

def ace(card):
    return card[0] == 'A'

def ace_x(player):
    if ace(player[0]) or ace(player[1]):
        return True
    else:
        return False

def suited(player):
    if player[0][-1] == player[1][-1]:
        return True
    else:
        return False

def conn_value(card):
    if card[0] == 'A':
        return 14
    if card[0] == 'K':
        return 13
    if card[0] == 'Q':
        return 12
    if card[0] == 'J':
        return 11
    if card[0] == '1':
        return 10
    else:
        return int(card[0])

def connected(player):
    if abs(conn_value(player[0]) - conn_value(player[1])) <= 2:
        return True
    else:
        return False

def high_card(player):
    return max(conn_value(player[0]), conn_value(player[1]))

def low_card(player):
    return min(conn_value(player[0]), conn_value(player[1]))


def strength(player):
    p_p = pocket_pair(player)
    b_w = two_broadway(player)
    a_x = ace_x(player)
    s_t = suited(player)
    c_n = connected(player)
    h_c = high_card(player)
    l_c = low_card(player)
    if p_p and b_w:
        return "ELITE"
    elif p_p or (a_x and s_t) or (b_w and s_t) or (a_x and b_w):
        return "VERY STRONG"
    elif b_w or a_x or (s_t and c_n and h_c >= 8):
        return "STRONG"
    elif h_c >= 13 or (h_c >= 10 and l_c >= 7 and (s_t or c_n)):
        return "ABOVE AVERAGE"
    elif (h_c >= 12 and l_c > 4) or (s_t and c_n) or (h_c >= 10 and l_c >= 5) or (h_c >= 8 and l_c > 4 and (s_t or c_n)):
        return "AVERAGE"
    elif h_c == 12 or (h_c >= 11 and l_c > 4) or (h_c >= 7 and l_c > 3 and (s_t or c_n)) or h_c >= 9:
        return "BELOW AVERAGE"
    elif (s_t or c_n) or h_c >= 8:
        return "WEAK"
    else:
        return "VERY WEAK"
    

