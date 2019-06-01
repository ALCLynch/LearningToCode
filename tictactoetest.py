 def main():
    user_input = get_user_input()
    valid_inputs = single_digit_numbers()
    
    while user_input != valid_inputs:
        print(Choose different space)
        user_input = get_user_input()

def get_user_input():
    try:
        return int(input('Enter a number between 1 and 9: '))
    except:
        print('Enter a number between 1 and 9')
        return get_user_input()


    

def single_digit_numbers =
    return int(0,9)

def input_letter1():
    letter = ("x")

def input_letter2():
    letter = ("o")

def play_again():
    print('Do you want to play again? (yes or no)')
    return input().startswith('yes')

def make_move(board,letter,move):
    board(1)

def winner(board,letter):


def player_score():
    count_x = 0
    count_o = 0
    

play_again()
        if not play_again()
        break

def play_again():
    print('Would you like to play again? (Yes or No):')
    return input().continueswith('y')



if __name__ == '__main__':
    main()