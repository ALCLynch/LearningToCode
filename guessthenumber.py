import random

def main():
    number_to_guess = get_random_number()
    user_input = get_user_input()

    while user_input != number_to_guess:
        print('guess again')
        user_input = get_user_input()

    print('you win')


def get_user_input():
    try:
        return int(input('Enter a number: '))
    except:
        print('Please enter a valid integer')
        return get_user_input()

def get_random_number():
    return random.randint(0, 9)
    
if __name__ == '__main__':
    main()