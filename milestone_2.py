#The random module is not imported in milestone_2.py. Make sure you import it to pick a random word from the list
#To accomplish this task, you will need to use the 'random' module. The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence.


# Step 1. Go to the first line of your file.

# Step 2. Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
#%%
import random
word_list = ["mango", "apple", "guava", "orange", "pear"]
print(word_list)
# pick a random choice from a list of strings.
word = random.choice(word_list)
print(word)

#%%
# Step 1. Using the input function, ask the user to enter a single letter.

# Step 2. Assign the input to a variable called guess.
print("Enter a single letter")
guess = input()
print(guess)

#%%
# Step 1. Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
# Step 2: In the body of the if statement, print a message that says "Good guess!".
# Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print ('Oops! That is not a valid input.')
