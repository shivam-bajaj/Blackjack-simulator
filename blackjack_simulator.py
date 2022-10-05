import random

'''
{"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
By taking default value of A is 11. When Ace is drawn, will check the suitable value 11 or 1.
'''
deck=[]
player_cards=[]
dealer_cards =[]
other_players_cards =[]


player_wins=0
dealer_wins=0
draw=0

def prepare_deck():

    global deck
    #4 Deck
    deck = ((list(range(2,12))+ [10]*3)*4)*4
    #Shuffle the deck
    random.shuffle(deck)


# Function to draw Card
def draw_card():
    global deck
    card = deck.pop()
    return card

def player(player_cards,dealer_cards,other_players_cards):
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)

    if player_sum>21:       # checking ace in the cards
        if 11 in player_cards:
            player_sum= player_sum-10
        else:
            return 0
    if player_sum>16:
        return 0
    if player_sum <12:
        return 1
    if player_sum <17 and  player_sum >12:
        if dealer_sum <7:
            return 0
        else:
            return 1

    if player_sum ==12:
        if dealer_sum < 4 or dealer_sum > 6:
            return 1
        else:
            return 0

def dealer(dealer_cards):
    dealer_sum  = sum(dealer_cards)
    if dealer_sum <17:
        return 1
    else:
        return 0


def check(cards):
    if sum(cards)> 21:
        return 0
    elif sum(cards) ==21:
        return 2
    else:
        return 1

#not necessary but can use for multplayers for   distribution of  cards
def initialize_game():
    global player_cards, dealer_cards
    player_cards.append(draw_card())
    #other_players_card.append(draw) #[[],[]] enumerate
    dealer_cards.append(draw_card())
    player_cards.append(draw_card())

'''
Let the game begin initialize the for loop here
'''
for i in range(0,1000):
    if len(deck)<100:
        prepare_deck()
    initialize_game()
    #print(f"player_cards { player_cards}")
    player_check=1
    #Player Game
    decision=player(player_cards,dealer_cards,other_players_cards)
    while(decision):
        card = draw_card()
        player_cards.append(card)
        #print(f"player_cards { player_cards}")
        decision=player(player_cards,dealer_cards,other_players_cards)
        player_check = check(player_cards)
        if player_check ==0:
            dealer_wins=dealer_wins+1
            break
        if player_check ==2:
            player_wins= player_wins+1
            break

    dealer_check=1
#Dealer Game
    #print(f"dealer_cards { dealer_cards}")
    # player check == 1 -> player is not busted or not have blackjack
    if player_check == 1:
        decision=dealer(dealer_cards)
        while(decision):
            card=draw_card()
            dealer_cards.append(card)
            #print(f"dealer_cards { dealer_cards}")
            decision = dealer(dealer_cards)
            dealer_check = check(dealer_cards)
            if dealer_check == 0:
                player_wins=player_wins+1
                break
            if dealer_check == 2:
                dealer_wins = dealer_wins+1
                break
                
    if player_check==1 and dealer_check ==1:
        if sum(dealer_cards) > sum(player_cards):
            dealer_wins = dealer_wins+1
        elif sum(dealer_cards) < sum(player_cards):
            player_wins = player_wins+1
        else:
            draw = draw+1

    player_cards=[]
    dealer_cards=[]
print(f"player win % -{player_wins/10}%")
print(f"dealer win % -{dealer_wins/10}%")
print(f"draw %  -{draw/10}%")
