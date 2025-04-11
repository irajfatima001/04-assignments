# Constant sentence starter
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    # Get the user inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Print the final sentence using f-string
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Required to call the main function
if __name__ == '__main__':
    main()
