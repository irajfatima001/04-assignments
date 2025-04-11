def read_phone_numbers():

    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # If the user inputs a blank line, stop adding entries
            break
        number = input("Number: ")
        phonebook[name] = number  # Store the name and number in the dictionary

    return phonebook


def print_phonebook(phonebook):

    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print each entry


def lookup_numbers(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook.")
            break  # Exits if the name is not found
        else:
            print(phonebook[name])

def main():
    # Step 1: Read phone numbers from the user and create a phonebook
    phonebook = read_phone_numbers()

    # Step 2: Print all entries in the phonebook
    print("Phonebook:")
    print_phonebook(phonebook)

    # Step 3: Allow the user to look up phone numbers by name
    print("\nPhone Number Lookup:")
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
