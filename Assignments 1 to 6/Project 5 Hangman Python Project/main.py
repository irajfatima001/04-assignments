#Hangman game
import random

# word list
word = ['forest', 'puzzle', 'python', 'rocket', 'ticket', 'planet', 'bridge', 'island', 'breeze', 'golden']

#chose a random word
word = random.choice(word)
guessed_word = ['_'] * len(word)
attempts = 6
guessed_letters = []


print("Welcome to Hangman! Try to guess the word.")

#game main loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print("You alraedy guessed that letter!")
    elif guess in word:
      print("correct!")
      for i, letter in enumerate(word):
        if letter == guess:
          guessed_word[i] = guess
    else:
      print("wrong guess!")
      attempts -= 1
    guessed_letters.append(guess)
    print(f"Remaining attempts: {attempts}")
#game over condition
if "_" not in guessed_word:
  print("\nCongratulations! You guessed the word:", word)
else:
  print("\nGame Over! The word was:" ,word)

