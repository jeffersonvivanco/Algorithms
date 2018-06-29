from functools import total_ordering
from time import perf_counter
import random

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
        return ' '.join(s_arr_new)

# TODO: Get file with many 5 letter words
# Below: Read 5 letter words from file, pick a word for the user to guess
# Below: Note: There are 5757 5 letter words in file_letter_words.txt. To get a random word first we pick a random number
# between 1 and 5757
random_word_line = random.randint(1, 5757)
# Then we read the file and stop at random_word_line and store that word
line_counter_start = 1
word_to_solve = 'buzzy'
with open('/Users/jeffersonvivanco/Documents/Algorithms/python/guessingWordProblem/five_letter_words.txt', 'rt') as f:
    for line in f:
        if random_word_line == line_counter_start:
            word_to_solve = line.strip() # picking a word
        line_counter_start += 1
word_to_solve_letter_object = []

# making an array of letter objects of the word picked
# we save index so later the guess function can determine if the word is correct
curr_index = 0
for l in word_to_solve:
    letter = Letter(l, curr_index)
    word_to_solve_letter_object.append(letter)
    curr_index += 1

word_to_solve_letter_object = sorted(word_to_solve_letter_object) # sorting list of list objects so we can compare with the string in the guess function

# Greeting, explain rules of the game
print("You have to try to guess the 5 letter word.\nYour first guess is free but each wrong guess afterwards is going to cost you $1000.")
print("In addition, for every millisecond the algorithm takes to determine if your guess is correct, you will be charged $10, sorry.")
print("However, for your first guess, the algorithm computation time is at no cost. Yayy!!\nYou have $10,000 to play the game.\nGood Luck!")

user_money = 10000 # money the user starts out with
is_first_guess = True # flag used to determine if it is the user's first guess, if so, it is free

while True: # loop is used for asking the user for the word
    if user_money <= 0: # if the user has 0 or less money, the game quits
        print('You have run out of money, no more guesses. The word was "' + word_to_solve+'"')
        break
    guess_word = input('Guess the word or "q" to give up\n')
    start = perf_counter() # starting the time to calculate how long the algorithm will take
    if guess_word == 'q':
        print('Nooo, please try again later, bye!')
        break
    if len(guess_word) != 5: # if the word is not equal to 5 characters, it counts as wrong
        if is_first_guess:
            is_first_guess = False
            print('You have to guess a 5 letter word but the 1st guess free so youre good, try again.')
            continue
        user_money -= 1000
        end = perf_counter()
        time_lapsed = round((end - start) * 1000, 2)
        user_money -= time_lapsed * 10
        print('The algorithm took ' + str(time_lapsed) + ' milliseconds, so it cost you $'+ str(time_lapsed * 10))
        print('You have to guess a 5 letter word, this counts as wrong which will cost you $1000\nYou have $' + str(user_money) + ' remaining')
        print('Please try again')
        continue
    guess_res = guess(guess_word)
    if word_to_solve == guess_res: # checks if the user's guess is correct
        end = perf_counter()
        time_lapsed = round((end - start) * 1000, 2)
        user_money -= time_lapsed * 10
        print('The algorithm took ' + str(time_lapsed) + ' milliseconds, so it cost you $' + str(time_lapsed * 10))
        print('You guessed it, the word is ' + guess_res + ' and you finished with $' + str(user_money) + ' dollars')
        break
    else: # if the user's guess is not correct
        if is_first_guess:
            is_first_guess = False
            print('Not correct sorry, but do not worry, first guess is free, try again, you got these letters right\n' + guess_res)
            continue
        user_money -= 1000
        end = perf_counter()
        time_lapsed = round((end - start) * 1000, 2)
        user_money -= time_lapsed * 10
        print('The algorithm took ' + str(time_lapsed) + ' milliseconds, so it cost you $'+ str(time_lapsed * 10))
        print('This wrong guess will cost you $1000\nYou have $' + str(user_money) + ' remaining')
        print('Please try again, you got these letters right\n' + guess_res)