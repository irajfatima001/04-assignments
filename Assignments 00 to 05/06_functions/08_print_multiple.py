def print_multiple(message: str, repeats: int):
    for i in range(repeats):  # Loop through and print the message 'repeats' times
        print(message)

def main():
    message = input("Please type a message: ")  # Get the message from the user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the repeat count from the user
    print_multiple(message, repeats)  # Call the function to print the message multiple times

if __name__ == '__main__':
    main()
