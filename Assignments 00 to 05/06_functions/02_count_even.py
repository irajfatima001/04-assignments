def count_even(lst):
    """
    Prints the number of even numbers in the given list.
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print("Number of even numbers:", count)


def get_list_of_ints():
    2

    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst


def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()
