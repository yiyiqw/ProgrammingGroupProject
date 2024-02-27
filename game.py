import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Set the maximum number of incorrect attempts

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Incorrect! {attempts} attempts left.")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if "_" in current_display:
        print(f"Sorry, you ran out of attempts. The word was {word_to_guess}.")

if __name__ == "__main__":
    hangman()
