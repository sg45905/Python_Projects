# define the the validate mathod to check player select valid move
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

# print what player or computer choose to play
def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

# define method to judge the results
def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'
