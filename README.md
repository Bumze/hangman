# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The development of the game entails creating variables in a list of fruits with basic Python commands. The game is programmed to generate random selection from the list using Python random() built-in functions. Users are then prompted to select a certain letter which is validated with Python len(0) and isalpha() functions. All modifications are staged, committed  and pushed to GitHub.


A class called hangman was created with (class Hangman). Inside the class, I created an init method to initialise the attributes of the class and passed in word_list and num_lives as parameters  with num_lives defaulting to a value to 5. Certain attributes were initialised as follows:

word: The word to be guessed, picked randomly from a word_list. This was implemented by importing the random module into the script. 
word_guessed: list - A list of the letters of the word. The list holds " " for each letter not yet guessed. As the letters are guessed correctly, the word_guessed list would be populated and the " " is replaced by the correct guess.  
num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet, completed with len of set function.
num_lives: int - The number of lives the player has at the start of the game.
word_list: list - A list of words.
list_of_guesses: list - A list of the guesses that have already been tried, set to an empty list initially.

Methods to check the guess called (check_guess) and the (ask_for_input) for requesting a letter from the player were created. The ask_for_input method was defined to run in a while loop which while true will allow the method to run indefintely except broken. Certain condition are created within the while loop,for which when satisfied, prompts a corresponding message. Finally, a function to play the game is created at same indentation as the class with the wordlist passed as a parameter. The function is called and game played.





