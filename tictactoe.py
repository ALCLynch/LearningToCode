# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52
def main():
    board = ['-' for i in range(1,10)]
    print_board(board)
    win_conditions = [(1, 2, 3),
                 (4, 5, 6),
                 (7, 8, 9),
                 (1, 4, 7),
                 (2, 5, 8),
                 (3, 6, 9),
                 (1, 5, 9),
                 (3, 5, 7)]
    
def print_board(board):
    print('       |       |  ')
    print('   {}   |   {}   |   {}'.format(board[0],board[1],board[2]))
    print('       |       |')
    print('-----------------------' )
    print('       |       |')
    print('   {}   |   {}   |   {}'.format(board[3],board[4],board[5]))
    print('       |       |')
    print('-----------------------')
    print('       |       |')
    print('   {}   |   {}   |   {}'.format(board[6],board[7],board[8]))
    print('       |       |')

if __name__ == '__main__':
    main()  