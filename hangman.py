import random
from woorden import woordenlijst


def get_word():
    woord = random.choice(woordenlijst)
    return woord.upper()


def play(woord):
    word_completion = "_" * len(woord)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Laten we galgje spelen!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nje hebt de letter", guess, "al geraden")
            elif guess not in woord:
                print(guess, "zit niet in het woord.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Dat klopt! De letter,", guess, "zit in het woord!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(woord) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(woord) and guess.isalpha():
            if guess in guessed_words:
                print("Je hebt het woord al geraden met: ", guess)
            elif guess != woord:
                print(guess, "is niet het woord.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = woord
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(" " + woord + ". Maybe next time!")


def display_hangman(tries):
    stages = [  #Laatste fout
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                #Vijfde fout
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                #Vierde fout
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                #Derde fout
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                #Tweede fout
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #Eerste fout
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #Beginfase
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()