def main():
    # Dictionary of fruit names and their corresponding prices
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

    # Initialize the total cost to zero
    total_cost = 0

    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        # Get the price of the current fruit
        price = fruits[fruit_name]

        # Ask the user how many of this fruit they want to buy
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))

        # Add the cost of this fruit to the total cost
        total_cost += (price * amount_bought)

    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")

# Python boilerplate to call the main function
if __name__ == '__main__':
    main()
