def main():
    print(is_even([5, 6, 7, 8]))

def is_even(arr):
    return sum(arr) % 2 == 0
    

if __name__ == '__main__':
    main()