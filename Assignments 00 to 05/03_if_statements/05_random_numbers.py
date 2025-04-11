import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1   # Minimum value of the range
MAX_VALUE = 100 # Maximum value of the range

def main():
    # Generate and print N_NUMBERS random numbers in the range [MIN_VALUE, MAX_VALUE]
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

if __name__ == '__main__':
    main()
