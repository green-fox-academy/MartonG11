
# Create a function named create palindrome following your current language's style guide.
#  It should take a string, create a palindrome from it and then return it.

x = "abcde"


def create_palindrome(word):
    y = word[ : :-1]
    print(y)

create_palindrome(x)