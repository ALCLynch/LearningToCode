# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52

win_conditions = [(1, 2, 3),
                 (4, 5, 6),
                 (7, 8, 9),
                 (1, 4, 7),
                 (2, 5, 8),
                 (3, 6, 9),
                 (1, 5, 9),
                 (3, 5, 7)]

def print_board(board):
    print('   |    |  ')
    print('{} | {} | {}'.format(board[1:3]))
    print('   |    |')
    print( '-----------' )
    print('   |    |')
    print('{} | {} | {}' .format(board[4:6]))
    print(   '|    |')
    print( '-----------')
    print(   '|   |')
    print(  '{} | {} | {}'.format(board[7:9]))
    print(  '|   |'



def new_game():
    print('Would you like another game? Type Yes or No:')
    return input.startswith('y')

def tic_tac_toe():
    board = ['' for  in range(10)]

if __name__ == '__main__':
    print('Tic Tac Toe')
    while True:
        ttt()
        if not new_game():
               