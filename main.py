import random

Deck = {
    #Hearts
    'A♥':11, 
    '2♥':2,
    '3♥':3,
    '4♥':4,
    '5♥':5,
    '6♥':6,
    '7♥':7,
    '8♥':8,
    '9♥':9,
    '10♥':10, 
    'J♥':10,
    'Q♥':10,
    'K♥':10,
    #Diamonds
    'A♦':11, 
    '2♦':2,
    '3♦':3,
    '4♦':4,
    '5♦':5,
    '6♦':6,
    '7♦':7,
    '8♦':8,
    '9♦':9,
    '10♦':10, 
    'J♦':10,
    'Q♦':10,
    'K♦':10,
    #Spades
    'A♠':11, 
    '2♠':2,
    '3♠':3,
    '4♠':4,
    '5♠':5,
    '6♠':6,
    '7♠':7,
    '8♠':8,
    '9♠':9,
    '10♠':10, 
    'J♠':10,
    'Q♠':10,
    'K♠':10,
    #Clubs
    'A♣':11, 
    '2♣':2,
    '3♣':3,
    '4♣':4,
    '5♣':5,
    '6♣':6,
    '7♣':7,
    '8♣':8,
    '9♣':9,
    '10♣':10, 
    'J♣':10,
    'Q♣':10,
    'K♣':10,
}

dealer_hand = [random.choices(list(Deck.keys())),random.choices(list(Deck.keys()))]
dealer_value = 0

for card in dealer_hand:
    current_card = "[]".join(card)
    dealer_value += Deck.pop(current_card)

player_hand = [random.choices(list(Deck.keys())),random.choices(list(Deck.keys()))]
player_value = 0

for card in player_hand:
    current_card = "[]".join(card)
    player_value += Deck.pop(current_card)

print(f"""

Dealer
-------------------------------------
{dealer_hand} Value = {dealer_value} 
-------------------------------------

Player
-------------------------------------
{player_hand} Value = {player_value} 
-------------------------------------
""")

#print("[]".join(dealer_hand[0]))