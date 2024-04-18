#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""

question = "enter a sentence."
phrase = input(question)

word = "password"
if word in phrase:
    print(f"the sentence contains password")
if word not in phrase:
    print(f"the sentence does not contain password")