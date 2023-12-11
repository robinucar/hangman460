import random
# Five fovorite fruits
word_list = ["Cherry", "Apricot", "Peach", "Apple", "Orange"]

# Assign the randomly generated word to a variable called word.
random_word = random.choice(word_list)

# Using the input function, ask the user to enter a single letter.

# Assign the input to a variable called guess.
user_guess_letter = input("Enter a single line please: ")
if len(user_guess_letter) == 1 and user_guess_letter.isalpha() == True:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")