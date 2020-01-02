import random

# Function that prints out the board. The board is gonna work like a num pad: having
# spaces that will take numbres from 1 to 9 from both players.


def display_board(board):
    print('\n'*100)
    print('      |     |')
    print('  '+board[1] + '   |  ' + board[2] + '  |  ' + board[3])
    print('      |     |')
    print('------------------')
    print('      |     |')
    print('  '+board[4] + '   |  ' + board[5] + '  |  ' + board[6])
    print('      |     |')
    print('------------------')
    print('      |     |')
    print('  '+board[7] + '   |  ' + board[8] + '  |  ' + board[9])
    print('      |     |')

# Function that will take the player's input and assign it to 'x' or 'o'.


def player_input():
    '''
    OUTPUT = (Choice PLayer1, Choice Player2)
    '''
    choice = ''
    while choice != 'x' and choice != 'o':
        choice = input(player1_name + ', choose x or o: ').lower()
    player1 = choice
    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
    return (player1, player2)

# Function that will take a markes ('x' or 'o'), a desired position (from 1 to 9), and will assign it
# to the board.


def place_marker(board, choice, position):
    board[position] = choice

# Function that takes the markers ('x' or 'o') in the boarder and checks if  the player has won.


def win_check(board, choice):
    return ((board[1] == choice and board[2] == choice and board[3] == choice) or
            (board[4] == choice and board[5] == choice and board[6] == choice) or
            (board[7] == choice and board[8] == choice and board[9] == choice) or
            (board[1] == choice and board[4] == choice and board[7] == choice) or
            (board[2] == choice and board[5] == choice and board[8] == choice) or
            (board[3] == choice and board[6] == choice and board[9] == choice) or
            (board[1] == choice and board[5] == choice and board[9] == choice) or
            (board[3] == choice and board[5] == choice and board[7] == choice))

# Function that randomly decides wich player goes first.


def choose_first():
    number = random.randint(0, 1)
    if number == 0:
        return player1_name
    else:
        return player2_name

# Function that returns a boolean indicating weather a space in the board is available.


def check_if_free(board, position):
    return board[position] == ' '

# Function that chacks if the board is full and returns a boolean.


def full_board_check(board):
    for x in range(1, 10):
        if check_if_free(board, x):
            return False
    return True

# Function that asks for the player's next position.


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not check_if_free(board, position):
        position = int(input('Choose a position from 1 to 9: '))
    return position

# Function that asks if the players want to play again.


def replay():
    choice = input('Do you want to play again? Enter yes or no: ')
    return choice == 'yes'

# Running the game.


print('Welcome to Tic Tac Toe!')

player1_name = input('Enter the name for player 1: ')
player2_name = input('Enter the name for player 2: ')

while True:
    the_board = [' ']*10
    choice_player1, choice_player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? yes or no? ')
    if play_game == 'yes':
        game = True
    else:
        game = False

    while game:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, choice_player1, position)
            # check if they won
            if win_check(the_board, choice_player1):
                display_board(the_board)
                print(player1_name + ' has won the game!!!')
                game = False
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Nobody won, it is a tie')
                    game = False
                    # nobody won and it's no tie, player2 turn
                else:
                    turn = 'Player 2'
        else:
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, choice_player2, position)
            # check if they won
            if win_check(the_board, choice_player2):
                display_board(the_board)
                print(player2_name + ' has won the game!!!')
                game = False
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Nobody won, it is a tie')
                    game = False
                    # nobody won and it's no tie, player2 turn
                else:
                    turn = 'Player 1'
    if not replay():
        break
