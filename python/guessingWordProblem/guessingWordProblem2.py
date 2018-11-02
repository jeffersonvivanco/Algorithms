import string
import guessingWordProblem.guess_word_helper as guess_word_helper
from time import perf_counter

guess_word_helper.get_word_to_solve()

print(' Starting guessing algorithm '.center(50, '='))
print('This algorithm guesses the 5 letter word chosen randomly from a list of words.')
print('The first guess the algorithm is charged nothing but afterwards it will cost it $1000.')
print("In addition, for every millisecond the algorithm takes to determine if the guess is correct, it will be charged $10.")
print('The algorithm starts out with $10,000. Hopefully it solves it before it runs out of money.')

letters = list(string.ascii_lowercase) # letter array used to get all the letters of the alphabet
stored_guess = ['_' for i in range(0, 5)]
stored_letters = []
num = 0
slice_start = 0
slice_end = 5

def make_guess(slice_start, slice_end):
    my_guess = ''.join(letters[slice_start:slice_end])
    guess_res = guess_word_helper.guess(my_guess)
    letter_index = 0
    for letter in guess_res:
        if letter != '_':
            stored_guess[letter_index] = letter
            stored_letters.append(letter)
        letter_index += 1

# this method also handles the case in which there is a z in the word
def find_repeated_letters(stored_letters):
    letters_search = stored_letters[0:2]
    stored_letters = stored_letters[2:]
    guess_2 = ''
    if len(letters_search) == 2:
        guess_2 = letters_search[0] * 2 + letters_search[1] * 3
    if len(letters_search) == 1:
        guess_2 = letters_search[0] * 5
    guess_res_2 = guess_word_helper.guess(guess_2)
    letter_index = 0
    for letter in guess_res_2:
        if letter != '_':
            stored_guess[letter_index] = letter
        letter_index += 1
    return stored_letters


# first guess is free
# we also use this first guess to setup the remaining guesses
# setup includes adding the alphabet to an array called letters
# setup includes initializing local variables to be used later by other guesses
algorithm_money = 10000
make_guess(slice_start, slice_end)
print('Guess ' + str(num + 1) + ' guessed word so far ' + ''.join(stored_guess))
num += 1
slice_start += 5
slice_end += 5

start = perf_counter()  # starting the time to calculate how long the algorithm will take

# 4 more guesses guesses
while num < 5:
    make_guess(slice_start, slice_end)
    print('Guess ' + str(num + 1) + ' guessed word so far ' + ''.join(stored_guess))
    num += 1
    slice_start += 5
    slice_end += 5
    algorithm_money -= 1000

if len(stored_letters) != 5:
    stored_letters.insert(0, 'z')
    while len(stored_letters) != 0:
        # more guesses to find the repeated letters
        stored_letters = find_repeated_letters(stored_letters)
        print('Guess ' + str(num + 1) + ' guessed word so far ' + ''.join(stored_guess))
        num += 1
        algorithm_money -= 1000


end = perf_counter()
time_lapsed = round((end - start) * 1000, 2)
algorithm_money -= time_lapsed * 10

# Below we use the word helper to get the word we are looking for
# to make sure the algorithm guessed the correct word
print('The word to guess was '+guess_word_helper.get_word())
print('Algorithm guessed '+''.join(stored_guess))
print('money left in the end ' + str(algorithm_money))
