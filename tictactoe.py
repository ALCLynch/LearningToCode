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
    win_conditions = [(0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6)]
    print('Player X has the first move!')
    player_x()
 


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

    
def choose_move(board):
    try:
        input_value = int(input())
        if input_value < 0 or input_value > 9:
            print('hey loser, thats outa range')
            return choose_move(board)
        if board[input_value] != '-':
            print('nice try dumbass, that is chosen already')
            return choose_move(board)
        return input_value
    except:
        print('moron, thats not a number')
        return choose_move(board)
    
board = board = ['-' for i in range(1,10)]
while True: # this loops forever
    print('      Tic Tac Toe!')
    print_board(board)
    print('Player 0, what move would like to make? ')
    m = choose_move(board)
    board[m] = "O"
    print('      Tic Tac Toe!')
    print_board(board)
    print('Player X, what move would like to make? ')

    m = choose_move(board)
    board[m] = "X"
    print('      Tic Tac Toe!')    
    print_board(board)
    print('Player 0, what move would like to make? ')

if __name__ == '__main__':
    main()  