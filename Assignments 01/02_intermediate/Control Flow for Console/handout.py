import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def get_valid_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").lower()
    return guess

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        print(f"Your number is {user_number}")
        guess = get_valid_guess()

        if (guess == "higher" and user_number > computer_number) or \
           (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")

    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("👀 Better luck next time!")

if __name__ == '__main__':
    main()
