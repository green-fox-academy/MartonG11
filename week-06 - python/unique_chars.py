# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases

def unique_characters(given_string):
    characters = list(given_string)
    return set([i for i in characters if characters.count(i) == 1])






print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]