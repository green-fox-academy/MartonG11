# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
# "What I cannot create, I do not understand"?

def fix_the(quote):
    quote[2], quote[5] = quote[5], quote[2]
    sentence = ' '.join(quote)
    return(sentence)

print(fix_the(words))


