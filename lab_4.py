import random

# Daftar kata-kata yang akan digunakan dalam permainan
words = ["python", "hangman", "programming", "computer", "gaming", "code", "challenge", "learning"]

def choose_word(words):
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    # Memilih kata secara acak
    secret_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(secret_word), "letters.")
    print(display_word(secret_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        # Validasi input pengguna
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Cek apakah huruf telah ditebak sebelumnya
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Tambahkan huruf yang ditebak ke dalam list
        guessed_letters.append(guess)

        # Periksa apakah huruf tersebut ada dalam kata rahasia
        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1

        # Tampilkan kata yang telah ditebak
        print(display_word(secret_word, guessed_letters))

        # Cek apakah pemain menang atau kalah
        if "_" not in display_word(secret_word, guessed_letters):
            print("Congratulations! You've guessed the word:", secret_word)
            break
        elif attempts == 0:
            print("Sorry, you ran out of attempts! The word was:", secret_word)
            break

        # Tampilkan sisa percobaan
        print("Attempts left:", attempts)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    hangman()
