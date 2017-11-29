# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

def longer(sentence):
    new_sen = sentence[ : 21] + "always takes longer than " + sentence[21: ]
    return new_sen

print(longer(quote))