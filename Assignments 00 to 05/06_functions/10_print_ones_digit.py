def print_ones_digit(num):
    # This function prints the ones digit of the given number
    print("The ones digit is", num % 10)

def main():

    num = int(input("Enter a number: "))
    # Call the function to print the ones digit of the number
    print_ones_digit(num)


if __name__ == '__main__':
    main()
