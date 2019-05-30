# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52
def main():
    print_board(True)
   

def print_board(board):
    print('|{}|{}|{}|'.format('board1','board2','board3'))
    print('-------')
    print('|{}|{}|{}|'.format('board4','board5','board6'))
    print('-------')
    print('|{}|{}|{}|'.format('board7','board8','board9'))





print('Tic Tac Toe!')







if __name__ == '__main__':
    main()
