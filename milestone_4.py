import random

class Hangman:
   
    def __init__(self, word_list, num_lives= 5):

        self.word_list = ["mango", "apple", "guava", "orange", "pear"]
        print(self.word_list)

        self.word = random.choice(self.word_list) # pick a random choice from a list of strings.
        self.word_guessed =[""]*len(self.word)
        self.num_letters = int(len(set(self.word)))  #{'p','e', 'a', 'r'} 
        self.num_lives = int(num_lives)
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! "+ guess + " is in the word")
        else:
            self.num_lives = self.num_lives - 1 
            print(f"Sorry, {guess} is not in the word.")    
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:   # Loop infinitely
            guess = input(" Guess a letter ")
            if len(guess) != 1 or guess.isalpha() is False:  
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            for i in range(len(self.word)): # for number in the range of length of letters
                if self.word[i] == guess:    #if letter at the index of word = guess 
                  self.word_guessed[i] = guess # populate word_guessed list at index i with guess
                  self.num_letters -= 1  # reduce number of unique letters in word not yet guessed
            else:
                  self.check_guess(guess)
                  self.list_of_guesses.append(guess)
            print(self.word_guessed)
           # print(self.num_letters) 
                #break

word_list = ["mango", "apple", "guava", "orange", "pear"]
res = Hangman(word_list)
res.ask_for_input()   