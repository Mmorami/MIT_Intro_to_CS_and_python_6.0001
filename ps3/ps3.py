# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

    The score for a word is the product of two components:

    The first component is the sum of the points for letters in the word.
    The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    # saving the word as all lowercase letters for consistency
    word = word.lower()
    # calculates the sum of the word's letters
    letters_val = 0
    for char in word:
        letters_val += SCRABBLE_LETTER_VALUES[char]
    # calculates the long word reward and saves it to a variable
    long_word_reward = 7*len(word) - 3*(n-len(word))
    # if the long word reward is greater than 1 multiply the sum of the letters' value by it, else return just the sum
    if long_word_reward > 1:
        return letters_val*long_word_reward
    return letters_val


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {}
    num_vowels = int(math.ceil(n / 3)) - 1

    hand['*'] = 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels+1, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # changing the input word to all lowercase letters as the dictionary is all lowercase as well
    word = word.lower()
    # creating a copy of the dictionary, as acting directly on the original one will change it even in the parent func
    new_hand = hand.copy()
    # iterating on the letters of the word
    for char in word:
        # if the letter is in the dictionary deduce one from it regardless of whether the
        # value is positive, negative or 0
        if char in new_hand.keys():
            new_hand[char] -= 1
            # if the value of the letter is either 0 or negative (can happen if the hand i get contains 0s)
            # then delete the letter from the dictionary
            if new_hand[char] <= 0:
                del new_hand[char]
    return new_hand

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # changing the input word to all lowercase letters as the dictionary is all lowercase as well
    word = word.lower()
    # creating a string to be mutated during the check
    ace_word = word
    # creating a dictionary with the frequency of the word's letters
    word_freq = get_frequency_dict(ace_word)

    # if the * char is in the word iterate over vowels and in each iteration replace the * with a new vowel
    if '*' in word:
        # a flag stating if the wildcard stands for a vowel and if so does such word exist
        is_wildcard_for_vowel = False
        for v in VOWELS:
            ace_word = word.replace('*', v)
            # if the word with * replaced by any vowel exist, change the flag to True and break out of the loop
            if ace_word in word_list:
                is_wildcard_for_vowel = True
                break
        if not is_wildcard_for_vowel:
            return False

    # check if the (without *) is in the word list or if the flag is false, meaning
    elif ace_word not in word_list:
        return False
    # checks if the hand contains the necessary letters to land the word
    for letter in word_freq.keys():
        if word_freq[letter] > hand.get(letter, -1):
            return False

    return True


#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # sum of letters in hand
    sum_of_letters = 0
    # iterates over the letters in hand and sum their values to know the length of the hand
    for letter in hand.keys():
        sum_of_letters += hand[letter]
    return sum_of_letters

    pass  # TO DO... Remove this line when you implement this function


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    total_points = 0
    # while hand is not an empty dictionary
    while bool(hand):
        # Display the hand
        display_hand(hand)
        # Ask user for input
        usr_input = input("Enter a word or '!!' to indicate you're finished: ")
        # If the input is two exclamation points end the game (break out of the loop)
        if usr_input == "!!":
            break
        # If the word is valid Tell the user how many points the word earned, and the updated total score
        if is_valid_word(usr_input, hand, word_list):
            round_points = get_word_score(usr_input, calculate_handlen(hand))
            total_points += round_points
            print(usr_input, "earned", round_points, "points.", "Total:", total_points)
        else:
            # Reject invalid word (print a message)
            print("This is not a valid word. You've been penalized. Please choose another word.")
        # update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, usr_input)
    # Game is over (user entered '!!' or ran out of letters), so tell user the total score
    if not bool(hand):
        print("\nRan out of letters.", end=' ')
    print("Total score for this hand:", total_points, "points")
    return total_points


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # creating new hand to be mutated as needed
    new_hand = hand.copy()
    # Defining the set of possible letters to draw as every letter in the alphabet
    new_letters_possible = VOWELS + CONSONANTS
    # iterates over each char in the dictionary and removes it from the possible chars to draw
    for char in hand.keys():
        new_letters_possible = new_letters_possible.replace(char, '')
    # chooses a random letter from the possible char set
    changed_letter = random.choice(new_letters_possible)
    # deletes the desired letter from the new hand and appends a new letter with the same amount
    del new_hand[letter]
    new_hand[changed_letter] = hand[letter]
    return new_hand


def substitute_hand_dialog(hand):
    """
    :param hand: dictionary, a full hand in the beginning of the game
    :return: a boolean determined if a letter was subbed, and a full hand subbed/not according to player's choice
    """
    # creating a hard copy of the hand
    new_hand = hand.copy()
    # initiating the change answer to an empty string
    change = ""
    # initiating not_subbed to True
    not_subbed = True
    # asking the player if they want to substitute a letter for another letter. keep asking while
    # no valid answer is given. The boolean adds an appropriate message for the player to note him the input isn't valid
    first = True
    while change != "y" and change != "n":
        if not first:
            print("Your answer is not valid. Please try again")
        else:
            first = False
        change = input("Would you like to substitute a letter? answer y for Yes or n for No: ")

    # if the player wants to substitute a letter keep asking for a letter. make sure the letter is a single alphabet
    # char that exist in the dictionary. The boolean adds an appropriate message for the player  to note him the input
    # isn't valid
    if change == "y":
        changed_letter = ""
        first = True
        while not changed_letter.isalpha() or len(changed_letter) != 1 or hand.get(changed_letter, -1) <= 0:
            if not first:
                print("Your answer is not valid, please try again. Enter a single letter that is in your hand.")
            else:
                first = False
            changed_letter = input("Which letter would you like to replace? ").lower()
        # substituting the desired letter
        new_hand = substitute_hand(hand, changed_letter)
        # changing not_subbed to False since the letter already subbed
        not_subbed = False
    return not_subbed, new_hand


def replay_hand():
    """
    :return: a boolean determined if a letter was subbed, and a full hand subbed/not according to player's choice
    """
    # initiating not_replayed to True
    not_replayed = True
    # initiating the replay answer to an empty string
    replay = ""
    # asking the player if they want to replay the hand. keep asking while
    # no valid answer is given. The boolean adds an appropriate message for the player to note him the input isn't valid
    first = True
    while replay != "y" and replay != "n":
        if not first:
            print("Your answer is not valid. Please try again")
        else:
            first = False
        replay = input("Would you like to replay the hand? answer y for Yes or n for No: ")

    # if the player wants to replay the hand
    if replay == "y":
        not_replayed = False
    return not_replayed


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands - V

    * Accumulates the score for each hand into a total score for the 
      entire series - V
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. - V

      This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future. - V

    * For each hand, ask the user if they would like to replay the hand. - V
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.

      This can only be done once during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. - V

      Replaying the hand does not count as one of the total number of hands the user initially
      wanted to play. - V

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # keeps asking for a valid number of hands to play, unless an integer is inserted
    while True:
        try:
            # takes user input for number of hands
            num_of_hands = int(input("Enter total number of hands: "))
            break
        except TypeError:
            print("You've inserted a non-integer.")
    # initiate total points in series
    total_points = 0
    # initiating the letter not substituted to True
    not_subbed = True
    # initiating the replayed taken option to True
    not_replayed = True
    # iterates over the number of hands instructed by the user. each hand iteration is a round of play
    for hand_number in range(num_of_hands):
        # initiating the round points to 0 with every new round
        round_points = 0
        # dealing a new hand to the player
        hand = deal_hand(HAND_SIZE)
        # creating a hard copy of the hand and displaying the hand to the player
        new_hand = hand.copy()
        display_hand(new_hand)
        # if the substitution option hasn't used yet ask the player
        if not_subbed:
            not_subbed, new_hand = substitute_hand_dialog(new_hand)
        # play the hand and assign the round points.
        round_points = play_hand(new_hand, word_list)
        print("----------------------------------------------------")
        # if the replay option hasn't used yet, ask the player
        if not_replayed:
            not_replayed = replay_hand()
            # if the not_replayed changed to False it means that the player chose to replay.
            if not not_replayed:
                # assign to round_points the max value between the previous round and the replay
                round_points = max(round_points, play_hand(hand, word_list))
        # sum the total points of all rounds
        total_points += round_points
        print("----------------------------------------------------")
    print("Total score for all hands:", total_points)
    

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

if __name__ == '__main__':
    word_list = load_words()
    # play_hand({'a': 1, 'c': 1, 'f': 1, 'i': 1, '*': 1, 't': 1, 'x': 1}, word_list)
    # print(substitute_hand({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'l'))
    play_game(word_list)
