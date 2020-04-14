def pig_latin(word):
    '''Converts a word into Pig Latin'''
    first_letter = word[0]
    rest_of_word = word[1:]
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u':
        return f"{word}way"
    else:
        return f"{rest_of_word}{first_letter}ay"


print(pig_latin('pig'))
print(pig_latin('owl'))
