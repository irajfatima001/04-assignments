MINIMUM_HEIGHT = 50  # Minimum height in arbitrary units (e.g., centimeters or inches)

def main():
    # Ask the user for their height
    height = float(input("How tall are you? "))

    # Check if the user is tall enough
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Call the main function
if __name__ == '__main__':
    main()
