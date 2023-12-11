import milestone_2

word_list = ["Cherry", "Apricot", "Peach", "Apple", "Orange"]
random_word = random.choice(word_list)
print(milestone_2.random_word)
def check_guess(guess):
    user_guess_letter = guess.lower()
    print(user_guess_letter)
    print(milestone_2.random_word)
    if user_guess_letter in milestone_2.random_word.lower():
        print(f"Good guess! {user_guess_letter} is in the word")
    else:
        print(f"Sorry, {user_guess_letter} is not in the word. Try again.")
       
def ask_for_input():
    user_guess_letter = input("Please enter a single letter: ")
    if len(user_guess_letter) == 1 and user_guess_letter.isalpha() == True:
        check_guess(user_guess_letter)
    else:
         print("Invalid letter. Please, enter a single alphabetical character.")

while True:
    ask_for_input()