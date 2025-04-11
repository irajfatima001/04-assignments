def main():
    # Get the year from the user
    year = int(input("Please input a year: "))

    # Leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call main function
if __name__ == '__main__':
    main()
