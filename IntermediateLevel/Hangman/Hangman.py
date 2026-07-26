
# Intermediate Level Task 
#Task 2:Hangman Game using Python

import random

# List of words with hints
words = {
    "python": "Programming Language",
    "computer": "Electronic Machine",
    "keyboard": "Used for Typing",
    "internet": "Global Network",
    "science": "Subject of Knowledge",
    "developer": "Person who writes code",
    "laptop": "Portable Computer",
    "shadowfox": "Internship Organization"
}

# Select random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Hangman stages
hangman = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

print("=" * 45)
print("      WELCOME TO HANGMAN GAME")
print("=" * 45)
print("Hint:", hint)

while wrong_guesses < max_wrong:

    print(hangman[wrong_guesses])

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Lives:", max_wrong - wrong_guesses)

else:
    print(hangman[max_wrong])
    print("\nGame Over!")
    print("Correct Word:", word)