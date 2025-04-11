
PROMPT: str = "What do you want? "
JOKE: str = (
    "Here is a joke for you! - Sophia was debugging her code for hours. "
    "Finally, she asked the AI: 'Why won’t my code run?' The AI replied: 'Because you forgot a semicolon... "
    "in Python.'")
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT)

    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == '__main__':
    main()
