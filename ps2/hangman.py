# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import numpy
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # inserting the string to a list in order to later use numpy array functions. each letter is an object in the list.
    secret_word = list(secret_word)
    # converting the list to a numpy array
    secret_word_array = numpy.array(secret_word)
    # reduces the array to unique values only. the list is then sorted in ascending order
    secret_word_array = numpy.unique(secret_word_array)

    c = 0
    for letter in letters_guessed:
        if letter in secret_word_array:
            c += 1
        if c == len(secret_word_array):
            break
    return c == len(secret_word_array)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # converting the secret word to a numpy array
    secret_word_array = numpy.array(list(secret_word))
    # reduces the array to unique values only. the list is then sorted in ascending order
    secret_word_array = numpy.unique(secret_word_array)
    # going through each unique letter in the secret word
    for char in secret_word_array:
        # if the letter is not in the guessed letter list then
        if char not in letters_guessed:
            secret_word = secret_word.replace(char, "_ ")
    return secret_word


def print_information(position, guesses, warnings, letters_guessed, secret_word):
    """
    :param position: string, 'before' indicates the info before the loop, 'after' indicates the info after the loop,
    'start_loop' indicates the info in the beginning of the loop, 'end_loop' indicates the info in the end of the loop
    :param guesses: int, the number of guesses left for the user
    :param warnings: int, number of warnings given in the beginning of the game
    :param letters_guessed: list, the list of all guessed letter
    :param secret_word: string, the secret word that is revealed so far
    :return: None. prints the appropriate info depends on the position
    """
    # start of the game info
    if position == "before":
        print("Welcome to the game of Hangman!")
        print("I am thinking of a word that is", len(secret_word), "letters long.")
        print("-------------------------------------------")
        print("You have", warnings, "warnings left.")
    # info for the beginning of every turn, before a guess is made
    elif position == "start_loop":
        # some more info for the player
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
    # info for the end of every turn, after guess is made
    elif position == "end_loop":
        print("The word so far is:", get_guessed_word(secret_word, letters_guessed))
        print("-------------------------------------------")
    # end of the game info
    elif position == "after":
        if guesses <= 0:
            print("Sorry buddy, no luck this time.")
            print("The secret word was:", secret_word)
        elif is_word_guessed(secret_word, letters_guessed):
            print("Congrats! you guessed the word right! Well done.")
            print("Your score is:", guesses * len(numpy.unique(numpy.array(list(secret_word)))))
    pass


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # gets all the lowercase letters in the alpha bet
    not_guessed = string.ascii_lowercase
    # iterates over every letter in the guessed letter list and replaces the letter in the alphabet (removes it)
    for letter in letters_guessed:
        not_guessed = not_guessed.replace(letter, '')
    return not_guessed


def is_user_valid_alphabet(user_input, warnings, guesses):
    """
    :param user_input: string, the raw input that the user entered
    :param warnings: int, number of warnings left to the user
    :param guesses: int, number of guesses left to the user
    :return: True if the input is valid and False if it isn't, in a tuple that contains warning num and guess num
    the code prints warnings as needed if the input is foul
    """
    if not user_input.isalpha():
        msg = "Your guess is not a valid letter."
        if warnings > 0:
            warnings -= 1
            print(msg, "You have", warnings, "warnings left.")
        else:
            guesses -= 1
            print(msg, "I'm done warning, i remove a guess. pay attention!")
        return False, warnings, guesses
    return True, warnings, guesses


def is_user_guess_exist(user_input, guess_list, warnings, guesses):
    """
    :param user_input: string, the raw input that the user entered
    :param guess_list: list of strings, list of all previous user guesses
    :param warnings: int, number of warnings left to the user
    :param guesses: int, number of guesses left to the user
    :return: True if the input is valid (char not in list) and False if it isn't, in a tuple that contains warning
    num and guess num
    the code prints warnings as needed if the input is foul
    """
    if user_input in guess_list:
        msg = "You've already guessed this letter"
        if warnings > 0:
            warnings -= 1
            print(msg, "You have", warnings, "warnings left.")
        else:
            guesses -= 1
            print(msg, "I'm done warning, i remove a guess. pay attention!")
        return False, warnings, guesses
    return True, warnings, guesses


def is_vowel(user_input):
    """
    :param user_input: string, the raw input that the user entered
    :return: return 2 if the letter is a vowel, and 1 if it is a consonant
    """
    vowels = "aeiou"
    if user_input in vowels:
        print("for wrong vowel you get 2 guesses off.")
        return 2
    print("for wrong consonant you get 1 guess off.")
    return 1


def main_game_code(user_guess, warnings, guesses, letters_guessed, secret_word):
    """
    :param user_guess: string, the raw input that the user entered
    :param warnings: int, number of warnings left to the user
    :param guesses: int, number of guesses left to the user
    :param letters_guessed: list of strings, list of all previous user guesses
    :param secret_word: string, the secret word to guess.
    :return: return the number of warnings, guesses and a list of the letters_guessed

    * this function does most of the main functionality of the game and called by the hangman function inside the loop
    """
    # checks if the user input is an alphabet. if not subtract warnings/guesses according to the rules
    is_valid = is_user_valid_alphabet(user_guess, warnings, guesses)
    if is_valid[0]:
        # converting the letters to lower case as the word list is all in lowercase
        user_guess = user_guess.lower()
        # checks if the user already guessed that letter. if he did subtract warnings/guesses according to the rules
        is_valid = is_user_guess_exist(user_guess, letters_guessed, warnings, guesses)
        if is_valid[0]:
            # appends the valid user guess to the guess list
            letters_guessed.append(user_guess)
            # prints an appropriate message depending whether the letter guessed was in the word or not
            if user_guess in secret_word:
                print(user_guess, "is in the word!")
            else:
                print("Sorry wrong guess, try another one.")
                guesses -= is_vowel(user_guess)
        else:
            warnings = is_valid[1]
            guesses = is_valid[2]
    else:
        warnings = is_valid[1]
        guesses = is_valid[2]

    return warnings, guesses, letters_guessed


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    """
    # initializing the number of guesses to 6 as the rules states, and the guessed letters to an empty list
    guesses = 6
    warnings = 3
    letters_guessed = []

    # Some printing for usability - information the user need to keep track of the game
    print_information("before", guesses, warnings, letters_guessed, secret_word)
    # keeps iterating until the word is guessed or no more guesses left
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        # some more info for the player
        print_information("start_loop", guesses, warnings, letters_guessed, secret_word)
        # takes the user guess
        user_guess = input("Please guess a letter: ")
        # main game function
        warnings, guesses, letters_guessed = main_game_code(user_guess, warnings, guesses, letters_guessed, secret_word)
        # some more info
        print_information("end_loop", guesses, warnings, letters_guessed, secret_word)

    # end of the game message
    print_information("after", guesses, warnings, letters_guessed, secret_word)
    pass


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, letters_guessed):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    letters_guessed: list of chars, all the chars that the user already tried to guess
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    """
    # get rid of all spaces that were inserted for usability
    my_word = my_word.replace("_ ", '_')
    # checks if the length of the two words equal. if not it returns False
    if len(my_word) != len(other_word):
        return False
    # iterates over all chars in my_word and keeps track of the index as well (see enumerate)
    for index, char in enumerate(my_word):
        # if the char in my_word is '_' then check if the letter in the same position in other_word is already revealed
        # later in my_word. if it is revealed then the hangman should've showed it to us and therefore it
        # wouldn't show as '_'. Hence this other_word cannot be the word we are looking for at this point of the game.
        if char == "_":
            if other_word[index] in letters_guessed:
                return False
            else:
                continue
        # if the loop gets here it means that the letter in my_word is known. if the char is not equal to the letter
        # in the same position in the other word then return False
        elif char != other_word[index]:
            return False
    # if the loop did not threw false until the end it means that every known letter in my_word is equal to the
    # corresponding letter in other_word, then return true as this word might be the one the player look for
    return True


def show_possible_matches(my_word, letters_guessed):
    """
    my_word: string with _ characters, current guess of secret word
    letters_guessed: list of chars, all the chars that the user already tried to guess
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """
    # initializing the string to be printed
    string_of_words = ""
    # iterates over every word in wordlist
    for word in wordlist:
        # if the word does not match - jump to next iteration. if it does not skip the iteration add the word to string
        if not match_with_gaps(my_word, word, letters_guessed):
            continue
        string_of_words += word + " "
    # after the loop ends print "No matches found" if nothing was added, else print out the words
    if string_of_words == "":
        print("No matches found")
    else:
        print("Possible word matches:", string_of_words)
    return None


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    """
    # initializing the number of guesses to 6 as the rules states, and the guessed letters to an empty list
    guesses = 6
    warnings = 3
    letters_guessed = []

    # Some printing for usability - information the user need to keep track of the game
    print_information("before", guesses, warnings, letters_guessed, secret_word)
    # keeps iterating until the word is guessed or no more guesses left
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        # some more info for the player
        print_information("start_loop", guesses, warnings, letters_guessed, secret_word)
        # takes the user guess
        user_guess = input("Please guess a letter: ")

        # if the user insert '*' get hint, else keep playing normally
        if user_guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
        else:
            warnings, guesses, letters_guessed = main_game_code(user_guess, warnings, guesses, letters_guessed, secret_word)
        # some more info
        print_information("end_loop", guesses, warnings, letters_guessed, secret_word)
    # end of the game message
    print_information("after", guesses, warnings, letters_guessed, secret_word)
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    # print(get_available_letters(['f', 'g', 'e', 'o', 'r', 'p', 'v', 'b']))

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman("else")#secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    # print(match_with_gaps("ta_ t", "tact", ['t', 'a', 'e', 'c', 'l', 'o']))
    # print(show_possible_matches("t_ _ t", ['t']))
    # print(show_possible_matches("t_ _ t", ['t', 'a']))
    # print(show_possible_matches("t_ _ t", ['t', 'a', 'o']))
    # print(show_possible_matches("t_ _ t", ['t', 'a', 'o', 'i']))
    # print(show_possible_matches("t_ _ t", ['t', 'a', 'o', 'i', 'e']))
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
