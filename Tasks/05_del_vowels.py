# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    splitString = list(string)
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    for letter in splitString:
        for vowel in vowels:
            if vowel == letter:
                splitString.remove(letter)
    return "".join(splitString)

print(disemvowel("hello world and I did it"))
#
# hll wrld nd  dd t
