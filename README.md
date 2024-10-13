# RobTheDealer

## Overview
![image](https://github.com/bassmm/RobTheDealer/assets/134802035/fa0427cd-32c5-4855-aff5-eca65a4021fd)

 - A python game based on the 'blackjack' card game, following the saem rules however with the objective of robbing the dealer of his money. Created with the use of the pygame library. 
>**NOTE:**  This project was intended to be a challange for myslef as i wanted to get better at python programming and overall improving my ability to translate ideas into code.

## Requirements
 - Python (3.x recommended)
 - Pygame library

## Installation
### Source
1. Ensure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/).
2. Install Pygame using pip:
    ``pip install pygame``
3. Clone the repository:
   ``git clone https://github.com/bassmm/RobTheDealer.git``

### Releases
1. Download the zip file from the releases tab.
2. Unzip the file
3. Run the executable titled "Game"
## Game Features
### Controls
Stand(S)

Hit(H)

(Enter bet value using input box)
### Rules
The game follows standard Blackjack rules, including:

- Player can 'Hit' or 'Stand.'
- Player wins if their hand total is closer to 21 than the dealer's without exceeding 21.
- Aces can count as 1 or 11 points.
- Face cards (Jack, Queen, King) count as 10 points.

### Interface

The game provides a graphical interface using Pygame for:

- Displaying cards for the player and dealer.
- Score display.
- Messages indicating game outcomes (win, lose, draw).

### Functionality
- Player can make decisions using keyboard or mouse inputs.
Dealer's moves are made using a probability system and some of randomness using the built-in 'random.py' library.
- Cards are drawn from a deck and distributed among player and dealer with card animations and sfx.
- Player and dealer scores are calculated and compared to determine the winner.
- Player and Dealer's money is kept track.

## Known Issues
- game may crash when dealer tries to take a card already take from the pile

## Future Improvements
- Clean up the code.
- Finish Game 

## Credits
Developer: Bassam
Pygame library: https://www.pygame.org/



