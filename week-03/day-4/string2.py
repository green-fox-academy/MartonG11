# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def new_char(sentence, old, new):
    if sentence == '':
        return ' '
    if sentence[0] == old:
        return new + new_char(sentence[1:], old, new)
    return sentence[0] + new_char(sentence[1:], old, new)

print(new_char('I have six boxes ', 'x', ''))