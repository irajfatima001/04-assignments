def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print(f"Wow, I can't wait to add this {word} to my vast collection of treasures!")
    elif part_of_speech == 1:
        # verb
        print(f"Wow! It's such a beautiful day, and it makes me want to {word}!")
    elif part_of_speech == 2:
        # adjective
        print(f"As I look out my window, the sky is vast and {word}!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Oops! The part of speech must be 0 (noun), 1 (verb), or 2 (adjective). Try again!")

def main():
    print("Let's make a sentence together! 😊")
    word = input("Please type a noun, verb, or adjective: ")
    print("Great choice! Now, tell me, is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
