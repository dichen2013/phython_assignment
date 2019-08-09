""" File name:   dfa.py
    Author:      <Di Chen>
    Date:        <Mar 9>
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.
                 
                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.
                 
                 It should be implemented for Exercise 3 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""


def load_dfa(dfa_file_name):
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
    """
    with open(dfa_file_name) as f:
        i = 0
        for line in f:
            if i == 0:

            initial_state  = line.split(" ")[1]

        type(f)
load_dfa("test1.dfa")

def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """