import random  # Import the random module to simulate dice rolls

NUM_SIDES = 6  # Number of sides on each die

def roll_dice():
    """Simulate rolling two dice and print the results"""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(f"\n🎲 Rolling the dice...")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

def main():
    while True:
        roll_dice()

        # Ask the user if they want to roll again
        choice = input("\nRoll again? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("🎲 Thanks for playing! Goodbye!")
            break  # Exit the loop


if __name__ == '__main__':
    main()
