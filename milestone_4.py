import random
class Hangman:
    def __init__(self, word_list, num_lives = 5 ):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        print(self.word)
        self.word_guessed =len(list(self.word.strip(""))) * ["_"]
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        print(self.num_letters)
        self.list_of_guesses = []
    def check_guess(self,guess):
        self.user_guess_letter = guess.lower()
        print(self.user_guess_letter)
        print(self.word)
        if self.user_guess_letter in self.word.lower():
            for index,letter in enumerate(self.word.lower()):
                if letter == self.user_guess_letter:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)
            self.num_letters = self.num_letters - 1
            print(self.num_letters)
            print(f"Good guess! {self.user_guess_letter} is in the word")
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {self.user_guess_letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} left...")
    def ask_for_input(self):
        while True:
            self.user_guess_letter = input("Please enter a single letter: ")
            if self.user_guess_letter.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif len(self.user_guess_letter) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.user_guess_letter in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.user_guess_letter)
                self.list_of_guesses.append(self.user_guess_letter)
                print(self.list_of_guesses)
game1 = Hangman(["Cherry", "Apricot", "Peach", "Apple", "Orange"])
game1.ask_for_input()