import random

# ASCII Art for the Hangman stages (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |

       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]

# Pool of secret words for the game
WORD_BANK = [
    "vegetable", "judgment", "martialregistery", "h", 
    "minceraft", "preparethyself"
]

def play_hangman():
    # Setup initial game state
    secret_word = random.choice(WORD_BANK).lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_lives = len(HANGMAN_STAGES) - 1

    print("Welcome to Hangman!")

    while incorrect_guesses < max_lives:
        print(HANGMAN_STAGES[incorrect_guesses])
        
        # Display the hidden word status (e.g., p _ t h _ n)
        displayed_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word: " + " ".join(displayed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the player won
        if "_" not in displayed_word:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            break

        # Process player input
        guess = input("Guess a letter: ").strip().lower()

        # Validate input mechanics
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single, valid alphabetical letter.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # Log the guess
        guessed_letters.add(guess)

        # Evaluate the guess
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses += 1
            print(f"Remaining attempts: {max_lives - incorrect_guesses}")

    # Handle loss condition
    if incorrect_guesses == max_lives:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"\n💀 Game Over! You ran out of tries. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()


