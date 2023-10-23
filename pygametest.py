import pygame, random
from sys import exit


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
    'jack_of_diamonds.png♦':10,
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

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('MostFairBlackJackGame')
clock = pygame.time.Clock()
title_font = pygame.font.Font(None, 16)

game_font = pygame.font.Font(None, 24)

table_surface = pygame.image.load('graphics/background_scaled.jpg')
title_text = title_font.render('MostFairBlackJackGame', True, 'White')
dealer_text = game_font.render('Dealer', True, 'Red')
dealer_card1 = pygame.image.load('graphics/cards/ace_of_clubs.png')
player_text = game_font.render('Player', True, 'Cyan')
player_card1 = pygame.image.load('graphics/cards/ace_of_hearts.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(table_surface,(0,0))
    screen.blit(title_text,(10,10))
    screen.blit(dealer_text,(30,30))
    screen.blit(dealer_card1,(30,60))
    screen.blit(player_text,(30,180))
    screen.blit(player_card1,(30,210))
    pygame.display.update()
    clock.tick(60)