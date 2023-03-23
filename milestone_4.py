import random
word_list = ["mango", "apple", "guava", "orange", "pear"]
print(word_list)
word = random.choice(word_list) # pick a random choice from a list of strings.
print(word)

def check_guess(guess):
    guess = input("Guess a letter")
    print(guess.lower())
    if len(guess) == 1 and guess.isalpha() and guess in word:
        print("Good guess!")
    else:
        print ('Oops! That is not a valid input.')

def ask_for_input():
    while True:   # Loop infinitely
        guess = input("Guess a letter")
        print(guess)

        if len(guess) == 1 and guess.isalpha() and guess in word:
            print(f"Good guess! {guess} is in the word.")
            break
        elif len(guess) != 1 or guess.isalpha() is False:  
            print("Invalid letter. Please, enter a single alphabetical character.")
        else: 
            print(f"Sorry, {guess} is not in the word. Try again.")
    check_guess(guess)
ask_for_input() 