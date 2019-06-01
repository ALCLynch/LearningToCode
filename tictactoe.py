# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52
def main():
    print('Thanks for playing!')

def check_end_tie():
    return ((board[0] == 'X' or board[0] == 'O')
    and (board[1] == 'X' or board[1] == 'O') 
    and (board[2] == 'X' or board[2] == 'O') 
    and (board[3] == 'X' or board[3] == 'O') 
    and (board[4] == 'X' or board[4] == 'O') 
    and (board[5] == 'X' or board[5] == 'O') 
    and (board[6] == 'X' or board[6] == 'O') 
    and (board[7] == 'X' or board[7] == 'O') 
    and (board[8] == 'X' or board[8] == 'O'))



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

def check_end_x():
    return ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X')
        or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X')
        or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X')
        or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X')
        or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X')
        or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')
        or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X')
        or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'))

def check_end_o():
    return ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O')
        or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O')
        or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O')
        or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O')
        or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O')
        or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')
        or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O')
        or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'))
    
def play_again():
    replay = input('New game (N) or quit (Q)? ')
    if replay == "N":
        return True
    if replay == "Q":
        return False
    else:
        print('Please answer N or Q! ')
        play_again()


def choose_move(board):
    try:
        input_value = int(input())
        if input_value < 0 or input_value > 8:
            print('hey loser, thats outa the board. try 0 to 8')
            return choose_move(board)
        if board[input_value] != '-':
            print('nice try dumbass, that is chosen already')
            return choose_move(board)
        return input_value
    except:
        print('moron, thats not a number')
        return choose_move(board)
count_o = 0
count_x = 0
count_tie = 0  
board = board = ['-' for i in range(1,10)]
while True: # this loops forever
    print('      Tic Tac Toe!')
    print_board(board)
    print('Player 0, what move would like to make? ')
    m = choose_move(board)
    board[m] = "O"
    print('      Tic Tac Toe!')
    print_board(board)
    if check_end_o():
        print('Congratulations Player 0!!! X is a loser!!!')
        count_o = count_o + 1
        print(count_x, ': Player X Victories')
        print(count_o, ': Player O Victories')
        print(count_tie, ': Number of ties')
        answer = play_again()
        if answer == True:
            board = ['-' for i in range(1,10)]
            continue
        else:
            break
    if check_end_tie() == True:
        print('Congratulations! You are both losers!!!')
        count_tie = count_tie + 1
        print(count_x, ': Player X Victories')
        print(count_o, ': Player O Victories')
        print(count_tie, ': Number of ties')
        answer = play_again()
        if answer == True:
            board = ['-' for i in range(1,10)] 
            continue
        else:
            break
    print('Player X, what move would like to make? ')
    m = choose_move(board)
    board[m] = "X"
    print('      Tic Tac Toe!')
    print_board(board)
    if check_end_x():
        print('Congratulations Player X!!! O is a loser!!!')
        count_x = count_x +1
        print(count_x, ': Player X Victories')
        print(count_o, ': Player O Victories')
        print(count_tie, ': Number of ties')
        answer = play_again()
        if answer == True:
            board = ['-' for i in range(1,10)]
            continue
        else:
            break
    if check_end_tie() == True:
        print('Congratulations! You are both losers!!!')
        count_tie = count_tie + 1
        print(count_x, ': Player X Victories')
        print(count_o, ': Player O Victories')
        print(count_tie, ': Number of ties')
        answer = play_again()
        if answer == True:
            board = ['-' for i in range(1,10)]
            continue
        else:
            break
    

if __name__ == '__main__':
    main()  