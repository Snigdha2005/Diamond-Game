import random

all_cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
scores = [0, 0]
player1_bids = []
player2_bids = []

def pick_diamond(cards):
    return random.choice(cards)
#print(pick_diamond(cards))

def adaptive_bidding_strategy(diamond_card, player_cards, opponent_bids):
    aggressiveness_threshold = 8

    if len(opponent_bids) != 0 and max([all_cards[_] for _ in opponent_bids]) > aggressiveness_threshold:
        return max(player_cards)
    elif all_cards[diamond_card] < 8:
        return min(player_cards)
    else:
        return max(player_cards)

def balanced_bidding_strategy(diamond_card, player_cards):
    if all_cards[diamond_card] >= 10:
        return max(player_cards)
    elif all_cards[diamond_card] <= 5:
        return min(player_cards)
    else:
        return max(player_cards)

def dynamic_adaptation_strategy(diamond_card, player_cards, opponent_aggressiveness, player_score):
    if opponent_aggressiveness == "aggressive" and player_score < 50:
        return min(player_cards)
    elif opponent_aggressiveness == "conservative" and player_score >= 50:
        return max(player_cards)
    else:
        return max(player_cards)

def bid_solver(diamond_card, player_cards, option, opponent_bids, scores):
    if option == 1:
        return adaptive_bidding_strategy(diamond_card, player_cards, opponent_bids)
    elif option == 2:
        return balanced_bidding_strategy(diamond_card, player_cards)
    elif option == 3:
        return dynamic_adaptation_strategy(diamond_card, player_cards, "aggressive", scores[0])
    elif option == 4:
        return random.choice(player_cards)
    return diamond_card

def remove_card_from_suit(suit, card):
    suit.remove(card)
    return suit

def update_suit(suits, cards):
    for i in range(len(suits)):
        suits[i].remove(cards[i])
    return suits

def player2_bid(diamond_card, player_cards, option, opponent_bids, scores, sub_option):
    if option == 1:
        return max(player_cards)
    elif option == 2:
        return min(player_cards)
    else:
        return bid_solver(diamond_card, player_cards, sub_option, opponent_bids, scores)

def scoreboard(diamond_card, bid1, bid2):
    global scores
    if bid1 > bid2:
        scores[0] = scores[0] + all_cards[diamond_card]
    elif bid2 > bid2:
        scores[1] = scores[1] + all_cards[diamond_card]
    else:
        scores = [scores[_] + all_cards[diamond_card] / 2 for _ in range(2)]
    return

def winner():
    m = max(scores)
    if m == scores[0] and m != scores[1]:
        return "Player 1"
    elif m == scores[1] and m != scores[0]:
        return "Player 2"
    return "Draw"

def main_game(option1, option2, sub_option2):
    cards = list(all_cards.keys())
    player1_cards = list(all_cards.keys())
    player2_cards = list(all_cards.keys())
    for i in range(13):
        diamond_card = pick_diamond(cards)
        bid1 = bid_solver(diamond_card, player1_cards, option1, player2_bids, scores)
        player1_bids.append(bid1)
        bid2 = player2_bid(diamond_card, player2_cards, option2, player1_bids, scores, sub_option2)
        player2_bids.append(bid2)
        [cards, player1_cards, player2_cards] = update_suit([cards, player1_cards, player2_cards], [diamond_card, bid1, bid2])
        print(diamond_card, bid1, bid2)
        scoreboard(diamond_card, bid1, bid2)
        print(scores)
    return winner()

'''
Player 1 options = 1 -> adaptive
                      2 -> balanced
                      3 -> dynamic adaptive
                      4 -> random
                      other -> same value as card
Player 2 options = 1 -> max(cards available)
                   2 -> min(cards available)
                   3 -> bids_solver -> player 1 sub_options
'''

option1 = 1
option2 = 4
sub_option2 = 5
print(main_game(option1, option2, sub_option2))
