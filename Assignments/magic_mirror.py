def magic_mirror(initial_word,rotated_word):
    if initial_word.islower() and rotated_word.islower() and len(initial_word)==len(rotated_word):
        temp=rotated_word*2
        if initial_word in temp:
            return 1
        else:
            return -1
    else:
        print('Give a valid input')

print(magic_mirror('sample','plesam'))

print(magic_mirror('saMple','plesam'))



def rotation(initial_word,rotated_word):
    (initial_word.split()).sort
    (rotated_word.split().sort)
    if initial_word==rotated_word:
        return 1
    else:
        return -1
rotation('bengaluru','luurbenga')