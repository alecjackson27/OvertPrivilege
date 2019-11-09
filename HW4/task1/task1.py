from .task1utils import *

# get user input
userInput = input("Please enter a word to base your password off of: ")

# create list of variations on password
# I'm gonna plan on making 5, may change as life goes on
list = create_list_of_passwords(userInput)

# output list of passwords

for word in list:
    print(word[0])