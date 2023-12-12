import random
class Hangman():
    """Hangman Class"""
    def __init__(self, word_list, num_lives = 5 ):
        """Initialise"""
        self.word_list = word_list # game word list
        self.num_lives = num_lives # number of lives
        self.word = random.choice(self.word_list) # random word within word_list
        print(self.word)
        self.word_guessed =len(list(self.word.strip(""))) * ["_"] # replace letters with underscore
        print(self.word_guessed)
        self.num_letters = len(set(self.word)) # count of unique characters
        print(self.num_letters)
        self.list_of_guesses = [] # letters already guessed
    def check_guess_letter(self,guess):
        """Checking user letter"""
        user_guess_letter = guess.lower() # letter which entered by user
        word = self.word.lower() # random word
        print(user_guess_letter)
        print(word)
        if user_guess_letter in word:
            for index,letter in enumerate(word):
                if letter == user_guess_letter:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)
            
            print("number of letters", self.num_letters)
            print(f"Good guess! {user_guess_letter} is in the word")
            self.num_letters = self.num_letters - 1
            
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {user_guess_letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left...")

    def ask_for_user_input(self):
        """Ask user to choice a letter and validation"""
        while True:
            user_guess_letter = input("Please enter a single letter: ") # ask user to enter a letter
            if user_guess_letter.isalpha() != True: # validation
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif len(user_guess_letter) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess_letter in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess_letter(user_guess_letter)
                self.list_of_guesses.append(user_guess_letter)
                print(self.list_of_guesses)
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You loss the game...")
            break
        elif num_lives > 0:
            game.ask_for_user_input()
            print("looping")
        elif num_lives > 0 and game.num_letters == 0:
            break
fruits = ["Orange", "Melon", "Apricot", "Cherry", "Peach"]
play_game(fruits)