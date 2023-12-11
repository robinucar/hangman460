import milestone_2

while True:

    user_guess_letter = input("Please enter a single letter: ")
    print(user_guess_letter)
    if user_guess_letter.isalpha():
        if user_guess_letter.lower() in milestone_2.random_word:
            print(f"Good guess! {user_guess_letter} is in the word")
        else:
            print(f"Sorry, {user_guess_letter} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
