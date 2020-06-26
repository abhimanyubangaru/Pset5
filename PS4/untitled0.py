#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:00:00 2020

@author: abhib
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''


    print(input)
    if len(sequence) > 3:
        print("You typed in more than three letters. Please re-run the program by entering a maximum of only three letters.")
    else:
        print("Computing...")
    if len(sequence) == 1:
        print(sequence)
    else:
        print("Computing...")
    if len(sequence) <= 1:
        #print([sequence])
        return [sequence]
    else:
        permutations = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_of_subsequence = get_permutations(next_chars)
        for seq in permutations_of_subsequence:
            for index in range(len(seq) + 1):
                new_sequence = seq[0:index] + first_char + seq[index:len(seq)+1]
                permutations.append(new_sequence)
           
        #print(permutations)
        return permutations
    
        


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    sequence = input("Please enter a string composed of a maximum of three letters") 
    print(get_permutations(sequence))
    
