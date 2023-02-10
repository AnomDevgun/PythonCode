import os
import random
import string as str


def player_input():
    marker = ''

    # Keep asking 1 player for X or O
    # Assign player 2 the other marker
    while marker != 'X' and marker != 'O':
        marker = input(f'Player 1, please choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def display_game(board):
    os.system('cls')
    print(f'Here is the current game:')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # Check all rows to see if there is the same marker,
    # similarly check columns
    # and diagonals
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    flip = random.randint(0, 1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position]==' '

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full  
    return True

def user_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9)'))
    return position

def replay():
    rep = input('Do you want to play again? Y or N: ').lower()
    if rep == 'y':
        return True
    else:
        return False







# While loop to keep running
print(f'Welcome to TIC-TAC-TOE in Python')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_game(theBoard)
            position = user_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_game(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_game(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_game(theBoard)
            position = user_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_game(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_game(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
