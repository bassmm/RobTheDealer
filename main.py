import pygame, random
from sys import exit

from regex import P

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

#INITIALIZATION CODE#
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('RobTheDealer')
clock = pygame.time.Clock()

#INITIAL CALCULATIONS#



#----GRAPHICS----#

#FONTS#
title_font = pygame.font.Font("graphics/fonts/Magicmedieval-pRV1.ttf", 48)
game_font = pygame.font.Font("graphics/fonts/Magicmedieval-pRV1.ttf", 24)

#BACKGROUND#
table_surface = pygame.image.load('graphics/background_wood.png').convert()

#TEXT#
title_text = title_font.render('RobTheDealer', True, 'White')
dealer_text = game_font.render('Dealer', True, 'White')
player_text = game_font.render('Player', True, 'White')

#BUTTONS#


#--CARDS--#

#DEALER
d_money = 1000
d_value = 0
d_hand = []
d_value_list = []

#searches d_hand, gets card and mathces it with value in Deck then pops it
for x in range(12):
    taken_card = random.choices(list(Deck))
    d_hand.append(taken_card)
    current_card = "[]".join(taken_card)
    d_value_list.append(Deck.pop(current_card))

d_card1 = pygame.image.load(f'graphics/cards/{"".join((d_hand[0]))}').convert_alpha()
d_card2hidden = pygame.image.load(f'graphics/cards/card_back.png').convert_alpha()
d_card2 = pygame.image.load(f'graphics/cards/{"".join((d_hand[1]))}').convert_alpha()
d_card3 = pygame.image.load(f'graphics/cards/{"".join((d_hand[2]))}').convert_alpha()
d_card4 = pygame.image.load(f'graphics/cards/{"".join((d_hand[3]))}').convert_alpha()
d_card5 = pygame.image.load(f'graphics/cards/{"".join((d_hand[4]))}').convert_alpha()
d_card6 = pygame.image.load(f'graphics/cards/{"".join((d_hand[5]))}').convert_alpha()
d_card7 = pygame.image.load(f'graphics/cards/{"".join((d_hand[6]))}').convert_alpha()
d_card8 = pygame.image.load(f'graphics/cards/{"".join((d_hand[7]))}').convert_alpha()
d_card9 = pygame.image.load(f'graphics/cards/{"".join((d_hand[8]))}').convert_alpha()
d_card10 = pygame.image.load(f'graphics/cards/{"".join((d_hand[9]))}').convert_alpha()
d_card11 = pygame.image.load(f'graphics/cards/{"".join((d_hand[10]))}').convert_alpha()
d_card12 = pygame.image.load(f'graphics/cards/{"".join((d_hand[11]))}').convert_alpha()

d_card_y = -100


d_value = d_value_list[0] + d_value_list[1]
#PLAYER#
p_money = 1000
p_value = 0
p_value_list = []
p_hand = []

for x in range(12):
    taken_card = random.choices(list(Deck))
    p_hand.append(taken_card)
    current_card = "[]".join(taken_card)
    p_value_list.append(Deck.pop(current_card))

p_card1 = pygame.image.load(f'graphics/cards/{"".join((p_hand[0]))}').convert_alpha()
p_card2 = pygame.image.load(f'graphics/cards/{"".join((p_hand[1]))}').convert_alpha()
p_card3 = pygame.image.load(f'graphics/cards/{"".join((p_hand[2]))}').convert_alpha()
p_card4 = pygame.image.load(f'graphics/cards/{"".join((p_hand[3]))}').convert_alpha()
p_card5 = pygame.image.load(f'graphics/cards/{"".join((p_hand[4]))}').convert_alpha()
p_card6 = pygame.image.load(f'graphics/cards/{"".join((p_hand[5]))}').convert_alpha()
p_card7 = pygame.image.load(f'graphics/cards/{"".join((p_hand[6]))}').convert_alpha()
p_card8 = pygame.image.load(f'graphics/cards/{"".join((p_hand[7]))}').convert_alpha()
p_card9 = pygame.image.load(f'graphics/cards/{"".join((p_hand[8]))}').convert_alpha()
p_card10 = pygame.image.load(f'graphics/cards/{"".join((p_hand[9]))}').convert_alpha()
p_card11 = pygame.image.load(f'graphics/cards/{"".join((p_hand[10]))}').convert_alpha()
p_card12 = pygame.image.load(f'graphics/cards/{"".join((p_hand[11]))}').convert_alpha()

p_card_y = 400



p_value = p_value_list[0] + p_value_list[1]

#--SFX--#
#--INTRO SEQUENCE--#
cardOpenPackage = pygame.mixer.Sound("sfx/cardOpenPackage1.wav")
cardTakeOutPackage = pygame.mixer.Sound("sfx/cardTakeOutPackage1.wav")
cardShuffle = pygame.mixer.Sound("sfx/cardShuffle.wav")

cardPlace1 = pygame.mixer.Sound("sfx/cardPlace1.wav")
cardPlace2 = pygame.mixer.Sound("sfx/cardPlace2.wav")
cardPlace3 = pygame.mixer.Sound("sfx/cardPlace3.wav")
cardPlace4 = pygame.mixer.Sound("sfx/cardPlace4.wav")

playintro = True
playsound1 = True
playsound2 = True
playsound3 = True
playsound4 = True

print(d_value)
print(p_value)

def intro_sequence():
    global playintro
    if playintro:
        pygame.display.update()
        cardOpenPackage.play()
        pygame.time.wait(1200)
        cardTakeOutPackage.play()
        pygame.time.wait(600)
        cardShuffle.play()
        pygame.time.wait(3200)
        playintro = False

#HIT/STAND FUNCTIONS#
hit_count = 0
def hit():
    global p_value
    global hit_count
    hit_count += 1
    new_card = random.choices(list(Deck.keys()))
    p_value += Deck.pop("[]".join(new_card))
    new_card_img = pygame.image.load(f'graphics/cards/{"[]".join(new_card)}').convert_alpha()
    
p1y = p_card_y
p2y = p_card_y
d1y = d_card_y
d2y = d_card_y
#MAIN CODE#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                hit()
                print (p_value)
    #RENDERING
    #BASE#
    screen.blit(table_surface,(0,0))
    screen.blit(title_text,(300,10))
    screen.blit(dealer_text,(30,60))
    screen.blit(player_text,(30,210))
    #DEALER#
    intro_sequence()

    if playsound1:
        cardPlace1.play()
        playsound1 = False
    if d_card_y < 90:
        d_card_y += 10
    
    if d_card_y == 90 and d_card_y < 90:
        if playsound2:
            cardPlace2.play()
            playsound2 = False
        d_card_y += 10
    screen.blit(d_card1,(30,d_card_y))
    screen.blit(d_card2hidden,(60,d_card_y))
    #PLAYER#
    if d_card_y == 90 and p_card_y > 240:
        if playsound3:
            cardPlace4.play()
            playsound3 = False
        p_card_y -= 10    
    screen.blit(p_card1,(30,p_card_y))
    if p_card_y == 240 and p_card_y > 240:
        if playsound4:
            cardPlace3.play()
            playsound4 = False
        p_card_y -= 10    
    screen.blit(p_card2,(60,p_card_y))
    #if hit_count == 1:
        #screen.blit(new_card_img,(90,240))
    pygame.display.update()
    clock.tick(60)