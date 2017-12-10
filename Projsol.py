#******************************************************************#
#
# TIC TAC TOE
#
#******************************************************************#

from IPython.display import clear_output
import random

# Function to display board
def display_bd(bd):
    clear_output()
    print('   |   |')
    print(' ' + bd[7] + ' | ' + bd[8] + ' | ' + bd[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bd[4] + ' | ' + bd[5] + ' | ' + bd[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bd[1] + ' | ' + bd[2] + ' | ' + bd[3])
    print('   |   |')


# Function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# function that takes, in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the bd
def place_marker(bd, marker, position):
    bd[position] = marker

# function that takes in a board and checks to see if someone has won
def win_check(bd, mark):
    return ((bd[7] == mark and bd[8] == mark and bd[9] == mark) or  # across the top
            (bd[4] == mark and bd[5] == mark and bd[6] == mark) or  # across the middle
            (bd[1] == mark and bd[2] == mark and bd[3] == mark) or  # across the bottom
            (bd[7] == mark and bd[4] == mark and bd[1] == mark) or  # down the middle
            (bd[8] == mark and bd[5] == mark and bd[2] == mark) or  # down the middle
            (bd[9] == mark and bd[6] == mark and bd[3] == mark) or  # down the right side
            (bd[7] == mark and bd[5] == mark and bd[3] == mark) or  # diagonal
            (bd[9] == mark and bd[5] == mark and bd[1] == mark))  # diagonal

# function that uses the random module to randomly decide which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# function that returns a boolean indicating whether a space on the board is freely available
def space_check(bd, position):
    return bd[position] == ' '

# function that checks if the bd is full and returns a boolean value
def full_bd_check(bd):
    for i in range(1,10):
        if space_check(bd, i):
            return False
    return True

# function that asks for a player's next position (as a number 1-9)
# and then uses the function from step 6 to check if its a free position
def player_choice(bd):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(bd, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

# function that asks the player if they want to play again and
# returns a boolean True if they do want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

############################################
#MAIN FUNCTION
############################################

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the bd
    thebd = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_bd(thebd)
            position = player_choice(thebd)
            place_marker(thebd, player1_marker, position)
            if win_check(thebd, player1_marker):
                display_bd(thebd)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_bd_check(thebd):
                    display_bd(thebd)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            display_bd(thebd)
            position = player_choice(thebd)
            place_marker(thebd, player2_marker, position)

            if win_check(thebd, player2_marker):
                display_bd(thebd)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_bd_check(thebd):
                    display_bd(thebd)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break