def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop through from 1 to num
        if num % i == 0:  # Check if i is a divisor of num
            print(i)

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call the helper function to print divisors

if __name__ == '__main__':
    main()