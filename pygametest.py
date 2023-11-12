import pygame, random
from sys import exit

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

#INITIALIZATION CODE
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('MostFairBlackJackGame')
clock = pygame.time.Clock()

#INITIAL CALCULATIONS#



#----GRAPHICS----#

#FONTS#
title_font = pygame.font.Font("graphics/fonts/Magicmedieval-pRV1.ttf", 48)
game_font = pygame.font.Font("graphics/fonts/Magicmedieval-pRV1.ttf", 24)

#BACKGROUND#
table_surface = pygame.image.load('graphics/background_wood.png')

#TEXT#
title_text = title_font.render('MostFairBlackJackGame', True, 'White')
dealer_text = game_font.render('Dealer', True, 'White')
player_text = game_font.render('Player', True, 'White')

#--CARDS--#

#DEALER
d_value = 0
d_hand = [random.choices(list(Deck.keys())),random.choices(list(Deck.keys()))]
d_card1 = pygame.image.load(f'graphics/cards/{"".join((d_hand[0]))}')
d_card2 = pygame.image.load(f'graphics/cards/card_back.png')

d_card1_y = -100
d_card2_y = -100

for card in d_hand:
    current_card = "[]".join(card)
    d_value += Deck.pop(current_card)

#PLAYER#
p_value = 0
p_hand = [random.choices(list(Deck.keys())),random.choices(list(Deck.keys()))]
p_card1 = pygame.image.load(f'graphics/cards/{"".join((p_hand[0]))}')
p_card2 = pygame.image.load(f'graphics/cards/{"".join((p_hand[1]))}')

p_card1_y = 400
p_card2_y = 400

for card in p_hand:
    current_card = "[]".join(card)
    p_value += Deck.pop(current_card)

#--SFX--#
#--INTRO SEQUENCE--#
cardOpenPackage = pygame.mixer.Sound("sfx/cardOpenPackage1.wav")


cardPlace1 = pygame.mixer.Sound("sfx/cardPlace1.wav")
cardPlace2 = pygame.mixer.Sound("sfx/cardPlace2.wav")
cardPlace3 = pygame.mixer.Sound("sfx/cardPlace3.wav")
cardPlace4 = pygame.mixer.Sound("sfx/cardPlace4.wav")

playsound1 = True
playsound2 = True
playsound3 = True
playsound4 = True

print(d_value)
print(p_value)
#MAIN CODE#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #RENDERING
    #BASE#
    screen.blit(table_surface,(0,0))
    screen.blit(title_text,(300,10))
    screen.blit(dealer_text,(30,60))
    screen.blit(player_text,(30,210))
    #DEALER#
    if playsound1:
        cardPlace1.play()
        playsound1 = False
    if d_card1_y < 90:
        d_card1_y += 10
    
    if d_card1_y == 90 and d_card2_y < 90:
        if playsound2:
            cardPlace2.play()
            playsound2 = False
        d_card2_y += 10
    screen.blit(d_card1,(30,d_card1_y))
    screen.blit(d_card2,(60,d_card2_y))
    #PLAYER#
    if d_card2_y == 90 and p_card1_y > 240:
        if playsound3:
            cardPlace4.play()
            playsound3 = False
        p_card1_y -= 10    
    screen.blit(p_card1,(30,p_card1_y))
    if p_card1_y == 240 and p_card2_y > 240:
        if playsound4:
            cardPlace3.play()
            playsound4 = False
        p_card2_y -= 10    
    screen.blit(p_card2,(60,p_card2_y))
    pygame.display.update()
    clock.tick(60)