# Create a function that takes the filepath (e.g. "da_vinci_code.txt") as an input, reads the given file, and counts the occurences of 0, 1 and x characters in it.
# The function should return a dictionary in which the searched characters are the keys and the number of their occurences are the values.
# Use the uploaded da_vinci_code.txt file in this folder on GitHub to test your program.


def countLetters(filename):
    counted_x = 0
    counted_1 = 0
    counted_0 = 0

    with open(filename,'r') as f:
        for char in f.read():
            if char == 'x':
                counted_x += 1
            elif char == '0':
                counted_0 += 1
            elif char == '1':
                counted_1 += 1
    return {'x':counted_x,'0':counted_0,'1':counted_1}

""" OR

def countLetters(filename):
    letters = {'x':0,'0':0,'1':0}

    with open(filename,'r') as f:
        for char in f.read():
            if char in letters:
                letters[char] += 1
    return letters

"""




# For example:
#
countedLetters = countLetters("da_vinci_code.txt")
print("0 occured " + str(countedLetters["0"]) + " times in the file.")
print("1 occured " + str(countedLetters["1"]) + " times in the file.")
print("x occured " + str(countedLetters["x"]) + " times in the file.")
# 
# Should print:
# 0 occured 3393 times in the file.
# 1 occured 3375 times in the file.
# x occured 3232 times in the file.