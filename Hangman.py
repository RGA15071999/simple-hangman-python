# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 12:52:52 2015

@author: Robert Gevorgyan
"""

# 
# Hangman
#

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a dictionary mapping letter counts to lists of valid words of
    that length. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    inFile.close()

    # wordlist: list of strings
    wordlist = string.split(line)
    word_dict = {}
    for word in wordlist:
        if word_dict.get(len(word)):
            word_dict[len(word)].append(word)
        else:
            word_dict[len(word)] = [word]
    print "  ", len(wordlist), "words loaded."
    return word_dict

def choose_word(word_dict, num_letters):
    """
    word_dict (dict): dictionary mapping integers to lists of words (strings)

    Returns a random word with num_letters letters.
    """
    return random.choice(word_dict[num_letters])


word_dict = load_words()

def write_it(let, out, wrd):
    blank = ''
    for i in range(0, len(out)):
        if out[i] != '_':
            blank += out[i]
        elif wrd[i] == let:
            blank += wrd[i]
        else:
            blank += '_'
    return blank

def hangman():
    n = input('Please input the length of the word you want to guess ')
    while n < 2 or n > 10:
        n = input('Please input the length of the word you want to guess ')
    chsn_word = choose_word(word_dict, n)
    guess_count = 2*n
    correct_word = False
    output = ''
    for i in range(0, n):
        output += '_'

    while guess_count > 0 and correct_word is False:
        print 'You have ', guess_count, ' guesses left.'
        letter = raw_input('Please guess a letter: ').lower()
        while len(letter) != 1:
            print 'Wrong input: There will be only one letter'
            letter = raw_input('Please guess a letter: ').lower()
        if letter in chsn_word:
            output =  write_it(letter, output, chsn_word)
            print 'Good guess:', output
        else:
            print 'Oops! That letter is not in my word:', output
            guess_count -= 1
        if output == chsn_word:
            correct_word = True
    if guess_count <= 0:
        print 'You lose, the word was ', '\'', chsn_word, '\''
    if correct_word:
        print 'Congratulations, you won!'

hangman()

