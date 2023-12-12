import random


class Hangman():

    '''
        Hangman Class
        This class is only one class to building a Hangman game.

        Attributes:
            1)  word: The word to be guessed, picked randomly from the word_list. 
                Remember to import the random module into your script
            2)  word_guessed: list - A list of the letters of the word, 
                with _ for each letter not yet guessed. 
            3)  num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

            4)  num_lives: int - The number of lives the player has at the start of the game.

            5)  word_list: list - A list of words

            6)  list_of_guesses: list - A list of the guesses that have already been tried. 
                Set this to an empty list initially
    '''

    def __init__(self, word_list, num_lives=5):
        """Initialise"""
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)

        self.word_guessed = len(list(self.word.strip(""))) * ["_"]
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess_letter(self, guess):
        """
            Checking user letter
            This method is validate the user letter. And print output according to user letter. 
            And it takes user letter as a parametr.
        """
        user_guess_letter = guess.lower()
        word = self.word.lower()
        print(user_guess_letter)
        if user_guess_letter in word:
            for index, letter in enumerate(word):
                if letter == user_guess_letter:
                    self.word_guessed[index] = letter
                    self.capitalize_first_letter(self.word_guessed)
                    print(self.word_guessed)
            print(f"Good guess! {user_guess_letter.upper()} is in the word")
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {user_guess_letter.upper()} is not in the word. Try again.")
            if self.num_lives > 1:
                print(f"You have {self.num_lives} lives left...")
            elif self.num_lives == 1:
                print(f"Your last chance... Only {self.num_lives} live left...")

    def ask_for_user_input(self):
        """
            ask_for_user_input

            This method is validate what user typed. It forces user to enter a single letter
        """
        while True:
            user_guess_letter = input("Please enter a single letter: ")
            if user_guess_letter.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif len(user_guess_letter) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess_letter in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess_letter(user_guess_letter)
                self.list_of_guesses.append(user_guess_letter)
                print(self.list_of_guesses)
                break

    def capitalize_first_letter(self, list):
        """
            Capitalize firs letter in a list
            This method is capitalising first element of a list.
            And it takes list as a parametr.
        """
        for item in range(len(list)):
            list[0] = list[0].upper()


def play_game(word_list):
    """ 
    play_game 
    This method is main independent method
    It takes word_list as a argument
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You loss the game...")
            break
        elif game.num_lives > 0 and game.num_letters == 0:
            print(f"Congratulations you win the game! The word is {game.word.upper()}...")
            break
        elif game.num_lives > 0:
            game.ask_for_user_input()


if __name__ == "__main__":
    words = ["Orange", "Melon", "Apricot", "Cherry", "Peach"]
    play_game(words)
