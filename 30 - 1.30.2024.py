''' Problem Statement: Write a function that checks whether a given string is a palindrome or not.
A palindrome is a word, phrase, number, or other sequences of characters that reads the same
forward and backward (ignoring spaces, punctuation, and capitalization).

Example: Input: "A man, a plan, a canal, Panama" Output: True (This sentence reads the same backward as forward)

Guidelines:

Any programming language can be used.

Consider optimizing your code for efficiency.

Don't forget to handle edge cases like empty strings, punctuation, and case sensitivity.'''

# since we can ignore spaces, punctuation, and capitilzation, function to clean the string entered
def is_palindrome(strng):
    cleaned_string = ''.join(char.lower() for char in strng if char.isalnum())

    # check if cleaned string is equal to the reverse of the cleaned string
    return cleaned_string == cleaned_string[::-1]

user_input = input("Please enter a phrase to see if it's a palindrome: ")
result = is_palindrome(user_input) # put string through function
print(result) # output True or False