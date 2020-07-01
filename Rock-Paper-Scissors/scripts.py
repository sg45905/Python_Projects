'''
@author - Sarthak Gupta
'''

import utils
import random

# take the player name as input
print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

# take player's hand as input
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

# validate hand
if utils.validate(player_hand):
    # if valid let the computer play

    # computer chooses any random move
    computer_hand = random.randint(0, 2)

    # print what player and the computer chose to play
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')

    # print the result
    result = utils.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    # if not valid raise error
    print('Please enter a valid number')
