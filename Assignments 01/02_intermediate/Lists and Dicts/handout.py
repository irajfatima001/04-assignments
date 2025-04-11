## Problem #1: List Practice
def main():
    # Create a list called fruit_list with initial fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit list:", fruit_list)

if __name__ == "__main__":
    main()


##-------------------------------------------------##

## Problem #2: Index Game
    
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range!"
    return lst[index]

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range!"
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Invalid indices!"
    return lst[start:end]

def main():
    # Sample list to work with
    sample_list = [5, 10, 15, 20, 25, "apple", "banana"]

    print("Welcome to the Index Game!")

    while True:
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the operation number: ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(sample_list, index)
            print(f"Element at index {index}: {result}")

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(sample_list, index, new_value)
            print(f"Updated list: {result}")

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(sample_list, start, end)
            print(f"Sliced list from {start} to {end}: {result}")

        elif choice == '4':
            print("Thanks for playing the Index Game!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

