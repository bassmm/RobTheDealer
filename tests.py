import random

#Deck Hash Map#
Deck = {
    #Hearts
    'ace_of_hearts.png':11, 
    '2_of_hearts.png':2,
    '3_of_hearts.png':3,
    '4_of_hearts.png':4,
    '5_of_hearts.png':5,
    '6_of_hearts.png':6,
    '7_of_hearts.png':7,
    '8_of_hearts.png':8,
    '9_of_hearts.png':9,
    '10_of_hearts.png':10, 
    'jack_of_hearts.png':10,
    'queen_of_hearts.png':10,
    'king_of_hearts.png':10,
    #Diamonds
    'ace_of_diamonds.png':11, 
    '2_of_diamonds.png':2,
    '3_of_diamonds.png':3,
    '4_of_diamonds.png':4,
    '5_of_diamonds.png':5,
    '6_of_diamonds.png':6,
    '7_of_diamonds.png':7,
    '8_of_diamonds.png':8,
    '9_of_diamonds.png':9,
    '10_of_diamonds.png':10, 
    'jack_of_diamonds.png':10,
    'queen_of_diamonds.png':10,
    'king_of_diamonds.png':10,
    #Spades
    'ace_of_spades.png':11, 
    '2_of_spades.png':2,
    '3_of_spades.png':3,
    '4_of_spades.png':4,
    '5_of_spades.png':5,
    '6_of_spades.png':6,
    '7_of_spades.png':7,
    '8_of_spades.png':8,
    '9_of_spades.png':9,
    '10_of_spades.png':10, 
    'jack_of_spades.png':10,
    'queen_of_spades.png':10,
    'king_of_spades.png':10,
    #Clubs
    'ace_of_clubs.png':11, 
    '2_of_clubs.png':2,
    '3_of_clubs.png':3,
    '4_of_clubs.png':4,
    '5_of_clubs.png':5,
    '6_of_clubs.png':6,
    '7_of_clubs.png':7,
    '8_of_clubs.png':8,
    '9_of_clubs.png':9,
    '10_of_clubs.png':10, 
    'jack_of_clubs.png':10,
    'queen_of_clubs.png':10,
    'king_of_clubs.png':10,
}

d_hand = [random.choices(list(Deck)),random.choices(list(Deck))]




print(d_hand)