from functools import total_ordering
import random

guess_word_helper_var = {}

# This class is to create letter objects.
# A Letter object represents a letter in the word the user has to guess.
# A Letter object consists of two properties, the letter as a string and the index as a number
# The index property is the index the letter is located in the word the user has to guess
# For example, if the word is fuzzy, a Letter object representing f will have f as its letter and 0 as its index
# The index is used in the algorithm to determine if a user guessed the correct letter and if so, we show them the
# correct index of the letter they guessed in the word to help them in their next guess
@total_ordering
class Letter():
    def __init__(self, letter, index):
        self.letter = letter
        self.index = index
    def __str__(self):
        return 'letter: ' + self.letter + ' index: ' + str(self.index)
    def __eq__(self, other):
        return self.letter == other.letter
    def __lt__(self, other):
        return self.letter < other.letter

# guess function which returns which letters in your guess you got correct
def guess(s):
    word_to_solve = guess_word_helper_var['word']
    word_to_solve_letter_object = guess_word_helper_var['letter_object']
    s_arr = sorted([l for l in s]) # sorts guess word so it can compare with the word to solve which is also sorted
    s_arr_new = ['_' for i in range(0, 5)] # creates an array of '_' elements so it can form a string later of the letters the user guessed correctly
    is_equal = True # flag used to speed up the process of returning whether the guess was right or not
    # Below: indeces are set to 0 so it can compare the first letters of the user's guess and the word to solve
    word_to_solve_index = 0
    s_arr_index = 0
    # Below: flag that if it does not get set to False in the while loop, it will terminate the while loop
    # We need this flag to tell the while loop to stop comparing letters.
    # If an index is checked, it is set to False, preventing the loop from terminating until all letters have been compared
    ready_to_break = True
    # Below: this flag is used to determine if the guess word equals the word to solve
    # We need this in case all the letters in the user's guess are correct, just not the right word
    # This flag is used to inform the user about why their guess is correct
    word_not_equal = s == word_to_solve
    while True: # loop that does the comparison of the letters in the user's guess and the word to solve
        ready_to_break = True
        if s_arr[s_arr_index] == word_to_solve_letter_object[word_to_solve_index].letter:
            s_arr_new[word_to_solve_letter_object[word_to_solve_index].index] = word_to_solve_letter_object[word_to_solve_index].letter
            if word_to_solve_index < 4:
                ready_to_break = False
                word_to_solve_index += 1
            if s_arr_index < 4:
                ready_to_break = False
                s_arr_index += 1
        elif s_arr[s_arr_index] > word_to_solve_letter_object[word_to_solve_index].letter:
            if word_to_solve_index < 4:
                ready_to_break = False
                word_to_solve_index += 1
            is_equal = False
        elif s_arr[s_arr_index] < word_to_solve_letter_object[word_to_solve_index].letter:
            if s_arr_index < 4:
                ready_to_break = False
                s_arr_index += 1
            is_equal = False
        else:
            is_equal = False
        if ready_to_break:
            break

    if is_equal: # if True, the user's guess was correct, just return the word to solve
        return word_to_solve
    else:
        s_arr_new_str = ' '.join(s_arr_new)
        if s_arr_new_str == word_to_solve and not word_not_equal:
            print("You didn't guess the word correctly, however all the letters in your word were correct just not in the\n right order, so we'll count it.")
        return ''.join(s_arr_new)

# Returns a random word from a file provided in project
def get_word_to_solve():
    word_to_solve_letter_object = []

    # Below: Read 5 letter words from file, pick a word for the user to guess
    # Below: Note: There are 5757 5 letter words in file_letter_words.txt. To get a random word first we pick a random number
    # between 1 and 5757
    random_word_line = random.randint(1, 5757)
    # Then we read the file and stop at random_word_line and store that word
    line_counter_start = 1
    word_to_solve = 'fuzzy'  # incase it fails to get the word
    with open('/Users/jeffersonvivanco/Documents/Algorithms/python/guessingWordProblem/five_letter_words.txt',
              'rt') as f:
        for line in f:
            if random_word_line == line_counter_start:
                word_to_solve = line.strip()  # picking a word
            line_counter_start += 1

    # making an array of letter objects of the word picked
    # we save index so later the guess function can determine if the word is correct

    curr_index = 0
    for l in word_to_solve:
        letter = Letter(l, curr_index)
        word_to_solve_letter_object.append(letter)
        curr_index += 1

    word_to_solve_letter_object = sorted(word_to_solve_letter_object)  # sorting list of list objects so we can compare with the string in the guess function
    guess_word_helper_var['letter_object'] = word_to_solve_letter_object
    guess_word_helper_var['word'] = word_to_solve

def get_word():
    return guess_word_helper_var['word']