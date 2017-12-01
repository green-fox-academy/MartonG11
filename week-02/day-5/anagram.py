# create a function named: anagram. = 2 strings: if string2 has the same letters as 
# string1, return: True. if not: false!
# and lower case = upper case

input1 = "god"
input2 = "dog"

def anagram(word1, word2):
    return clean(word1) == clean(word2)

def clean(string):
    return ''.join(sorted(string)).lower().split()

print(anagram(input1, input2))
