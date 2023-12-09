import pygame, random
from sys import exit


#Deck Hash Map#
Deck = {
    #Hearts
    'ace_of_hearts.png':1, 
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
    'ace_of_diamonds.png':1, 
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
    'ace_of_spades.png':1, 
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
    'ace_of_clubs.png':1, 
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
bet_input_font = pygame.font.Font("graphics/fonts/Magicmedieval-pRV1.ttf", 32)

#BACKGROUND#
table_surface = pygame.image.load('graphics/background_wood.png').convert()

#TEXT#
title_text = title_font.render('RobTheDealer', True, 'White')
dealer_text = game_font.render('Dealer', True, 'White')
player_text = game_font.render('Player', True, 'White')
bet_input_title = game_font.render ('Bet Amount:',True, 'White')
click_to_continue = game_font.render ('click anywhere to continue',True, 'White')


#MONEY SYSTEM#
d_money = 1000
p_money = 1000

d_money_text = game_font.render(f"${d_money}", True, (143, 197, 111))

p_money_text = game_font.render(f"${p_money}", True, (143, 197, 111))


#--CARDS--#

# Ace is considered as 11 only once and rest of the time it is taken as 1
d_first_ace = True
p_first_ace = True

#DEALER
d_value = 0
d_hand = []
d_value_list = []

#searches hand, gets card and mathces it with value in Deck then pops it
def assign_card_to_hand(hand:list,value_list:list):
    global Deck
    for x in range(12):
        taken_card = random.choices(list(Deck))
        hand.append(taken_card)
        current_card = "[]".join(taken_card)
        value_list.append(Deck.pop(current_card))


assign_card_to_hand(d_hand,d_value_list)


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
if d_value_list[0] == 1 or d_value_list[1] == 1:
    d_first_ace = False
    d_value += 10

#PLAYER#
p_value = 0
p_value_list = []
p_hand = []

assign_card_to_hand(p_hand,p_value_list)


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
if p_value_list[0] == 1 or p_value_list[1] == 1:
    p_first_ace = False
    p_value += 10

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
print('--')
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


def pause():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False


#HIT/STAND FUNCTIONS#
hit_count = 0
dhit_count = 0
def hit():
    global p_value, hit_count, p_first_ace
    hit_count += 1
    if p_value_list[(1+hit_count)] == 1 and p_first_ace:
        p_first_ace = False
        p_value += 11
    else:
        p_value += p_value_list[(1+hit_count)]
    if p_value > 21 and p_first_ace == False:
            p_value -= 10
            p_first_ace = True
    


    #for maintenance
    print(f'''
{d_value}
{d_value_list}
{p_value}
{p_value_list}

''')



def dealer_hit():
    global d_value, dhit_count, d_first_ace
    screen.blit(d_card2,(60,100))
    while d_value < 17:
        dhit_count += 1
        if d_value_list[(1+dhit_count)] == 1 and d_first_ace:
            d_first_ace = False
            d_value += 11
        else:
            d_value += d_value_list[(1+dhit_count)]
        if d_value > 21 and d_first_ace == False:
            d_value -= 10
            d_first_ace = True


def display_cards_after_hit():
    global hit_count
    global dhit_count
    if hit_count > 0:
        screen.blit(p_card3,(90,250))
    if hit_count > 1:
        screen.blit(p_card4,(120,250))
    if hit_count > 2:
        screen.blit(p_card5,(150,250))
    if hit_count > 3:
        screen.blit(p_card6,(180,250))
    if hit_count > 4:
        screen.blit(p_card7,(210,250))
    if hit_count > 5:
        screen.blit(p_card8,(240,250))
    if hit_count > 6:
        screen.blit(p_card9,(270,250))
    if hit_count > 7:
        screen.blit(p_card10,(300,250))
    if hit_count > 8:
        screen.blit(p_card11,(330,250))
    if hit_count > 9:
        screen.blit(p_card12,(360,250))

    if dhit_count > 0:
        screen.blit(d_card3,(90,100))
    if dhit_count > 1:
        screen.blit(d_card4,(120,100))
    if dhit_count > 2:
        screen.blit(d_card5,(150,100))
    if dhit_count > 3:
        screen.blit(d_card6,(180,100))
    if dhit_count > 4:
        screen.blit(d_card7,(210,100))
    if dhit_count > 5:
        screen.blit(d_card8,(240,100))
    if dhit_count > 6:
        screen.blit(d_card9,(270,100))
    if dhit_count > 7:
        screen.blit(d_card10,(300,100))
    if dhit_count > 8:
        screen.blit(d_card11,(330,100))
    if dhit_count > 9:
        screen.blit(d_card12,(360,100))
is_stand = False


def stand():
    global is_stand, d_money, p_money, hit_count, d_hand, p_hand, p_value_list, d_value_list, p_value, d_value, Deck, nobet, dhit_count, p_first_ace, d_first_ace
    is_stand = True
    dealer_hit()
    display_cards_after_hit()
    screen.blit(click_to_continue,(0,0))
    pygame.display.update()
        #for maintenance
    print(f'''
{d_value}
{d_value_list}
{p_value}
{p_value_list}

''')
    pause()



    if p_value > d_value or d_value > 21:
        if p_value <= 21:
            d_money -= bet_value
            p_money += bet_value
    if d_value > p_value or p_value > 21:
        if d_value <= 21:
            d_money +=  bet_value
            p_money -= bet_value

    p_first_ace = True
    d_first_ace = True
    hit_count = 0
    dhit_count = 0
    p_value = 0
    d_value = 0
    d_value_list = []
    p_value_list = []
    p_hand = []
    d_hand = []
    Deck = {'ace_of_hearts.png':1, '2_of_hearts.png':2,'3_of_hearts.png':3,'4_of_hearts.png':4,'5_of_hearts.png':5,'6_of_hearts.png':6,'7_of_hearts.png':7,'8_of_hearts.png':8,'9_of_hearts.png':9,'10_of_hearts.png':10, 'jack_of_hearts.png':10,'queen_of_hearts.png':10,'king_of_hearts.png':10,'ace_of_diamonds.png':1, '2_of_diamonds.png':2,'3_of_diamonds.png':3,'4_of_diamonds.png':4,'5_of_diamonds.png':5,'6_of_diamonds.png':6,'7_of_diamonds.png':7,'8_of_diamonds.png':8,'9_of_diamonds.png':9,'10_of_diamonds.png':10, 'jack_of_diamonds.png':10,'queen_of_diamonds.png':10,'king_of_diamonds.png':10,'ace_of_spades.png':1,'2_of_spades.png':2,'3_of_spades.png':3,'4_of_spades.png':4,'5_of_spades.png':5,'6_of_spades.png':6,'7_of_spades.png':7,'8_of_spades.png':8,'9_of_spades.png':9,'10_of_spades.png':10,'jack_of_spades.png':10,'queen_of_spades.png':10,'king_of_spades.png':10,'ace_of_clubs.png':1, '2_of_clubs.png':2,'3_of_clubs.png':3,'4_of_clubs.png':4,'5_of_clubs.png':5,'6_of_clubs.png':6,'7_of_clubs.png':7,'8_of_clubs.png':8,'9_of_clubs.png':9,'10_of_clubs.png':10, 'jack_of_clubs.png':10,'queen_of_clubs.png':10,'king_of_clubs.png':10,}

    assign_card_to_hand(d_hand,d_value_list,)
    assign_card_to_hand(p_hand,p_value_list)
    
    d_value = d_value_list[0] + d_value_list[1]
    p_value = p_value_list[0] + p_value_list[1]
    if d_value_list[0] == 1 or d_value_list[1] == 1:
        d_first_ace = False
        d_value += 10
    if p_value_list[0] == 1 or p_value_list[1] == 1:
        p_first_ace = False
        p_value += 10

    nobet = True

    #for maintenance
    print(f'''
{d_value}
{d_value_list}
{p_value}
{p_value_list}

''')


#Value Input#
user_text = ''
input_rect = pygame.Rect(30,200,400,40)
bet_value = 0


nobet = True

def bet_screen():
    global nobet
    global user_text
    global bet_value
    active = False
    active_colour = pygame.Color('White')
    inactive_colour = pygame.Color('Grey')
    box_colour = inactive_colour
    while nobet:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                    box_colour = active_colour
                else:
                    box_colour = inactive_colour
                    active = False
            
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

                if event.key == pygame.K_RETURN:
                    bet_value = int(user_text)
                    user_text = ''
                    nobet = False
        
        # Base
        screen.blit(table_surface,(0,0))
        screen.blit(title_text,(300,10))
        screen.blit(dealer_text,(30,60))
        screen.blit(player_text,(30,100))
        screen.blit(d_money_text,(100,60))
        screen.blit(p_money_text,(100, 100))
        screen.blit(bet_input_title,(30,170))
        # Text Box 
        pygame.draw.rect(screen, box_colour, input_rect, 2)
        text_surface = bet_input_font.render(user_text,True,(255,255,255))
        screen.blit(text_surface,(input_rect.x + 5,input_rect.y + 2))
        input_rect.w = max(100,(text_surface.get_width() + 10))
        pygame.display.update()





#MAIN CODE#
while True:

    bet_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                hit()


            if event.key == pygame.K_s:
                stand()

    if p_value > 21:
        stand()
    #refresh card images
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
    
    d_money_text = game_font.render(f"${d_money}", True, (143, 197, 111))
    p_money_text = game_font.render(f"${p_money}", True, (143, 197, 111))
    
    # RENDERING
    # Base
    screen.blit(table_surface,(0,0))
    screen.blit(title_text,(300,10))
    screen.blit(dealer_text,(30,60))
    screen.blit(player_text,(30,210))
    screen.blit(d_money_text,(100,60))
    screen.blit(p_money_text,(100, 210))

    # Dealer
    screen.blit(d_card1,(30,100))
    screen.blit(d_card2hidden,(60,100))
    # Player 
    screen.blit(p_card1,(30,250)) 
    screen.blit(p_card2,(60,250))
    

    display_cards_after_hit()
    
    is_stand = False
    pygame.display.update()
    clock.tick(60)
