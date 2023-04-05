'''
Various Functions
Toaster914
4/5/23
'''

import random

def count_occurences(string_from, string_in):
    '''
    Finds if a word occures in the string, and reports how many times it occurs.
    string_in: the word to Find
    string_from: the string to find from
    retuns: The times the word occurs
    '''
    times = 0
    string_from = string_from.lower()
    string_in = string_in.lower()
    words = string_from.split()

    for i in range(0, len(words)):
        if string_in in words[i]:
            times += 1

    return times

def occurence_indexes(string_from, string_in):
    '''
    Finds if a word occures in the string, and reports the index it is at.
    string_in: the word to Find
    string_from: the string to find from
    returns: the indexes the word occurs
    '''
    indexes = []
    string_from = string_from.lower()
    string_in = string_in.lower()
    words = string_from.split()

    for i in range(0, len(words)):
        if string_in in words[i]:
            indexes.append(i)

    return indexes

def palindrome(word):
    '''
    Checks if a word is a palindrome
    returns: True or False
    '''
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    if reversed_word == word:
        return True
    return False

def minimum(numbers_list):
    '''
    Gets the lowest number in a list
    returns: The minimum
    '''
    minimum = numbers_list[0]
    for i in range(0, len(numbers_list)):
        if numbers_list[i] < minimum:
            minimum = numbers_list[i]
    return minimum

def maximum(numbers_list):
    '''
    Gets the highest number in a list
    returns: The maximum
    '''
    maximum = numbers_list[0]
    for i in range(0, len(numbers_list)):
        if numbers_list[i] > maximum:
            maximum = numbers_list[i]
    return maximum

def all_same(numbers_list):
    '''
    Checks if all numbers in a list are the all_same
    returns: True or False
    '''
    for i in range(0, len(numbers_list)):
        if numbers_list[0] != numbers_list[i]:
            return False
    return True

def mean(numbers_list):
    '''
    Finds the mean in a list
    retuns: the mean
    (its returning a average)
    '''
    total = 0
    times = 0
    for number in numbers_list:
        total += number
        times += 1
    mean = total / times
    return mean

def scramble(word):
    '''
    Scrambles the word.
    returns: the scrambled word
    '''
    new_word = ""
    used_indexes = []
    while len(new_word) < len(word):
        index = random.randint(0, len(word) - 1)
        if index not in used_indexes:
            new_word += word[index]
            used_indexes.append(index)
    return new_word

def median(numbers):
    '''
    Gets the median of a list of numbers
    returns: the median
    '''
    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    return numbers[middle_index]

def double(num_list):
    '''
    Doubles the values in num_list.
    '''
    for i in range(0, len(num_list)):
        num_list[i] *= 2

def display_border(symbol, amount):
    '''
    Displays a border using the passed symbol. Repeats symbol the passed
    amount of times. Automatically goes to next line.
    '''
    for i in range(0, amount):
        print(symbol, end="")
    print()

