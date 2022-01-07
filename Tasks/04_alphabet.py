# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
#
# Example
#
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

# First solve:

alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

your_text = input("Enter text: ")
new_list = list(your_text)

outcome = []

for i in new_list:
    for j in alphabet:
        if i == j:
            outcome.append(alphabet[j])

print(*outcome)
#
# Hello everyone and goodbye
# 5 12 12 15 5 22 5 18 25 15 14 5 1 14 4 7 15 15 4 2 25 5

# Second solve:

# def alphabet_position(text): #function name: alphabet_position, function parameter: text
#     output = '' #the return var
#     for ch in text.lower(): #for each character labelled ch in the lower case version of text
#         if ch.isalpha(): #if it meets the criteria of an alphabetical letter
#             output = output + str(ord(ch) - 96) + ' ' #find its value, taken from stackoverlfow
#     output = output.strip() #strip the bare space
#     return output #return the output value










