#!/usr/bin/env python
# HanoiMoves.py
# Author: Lijuan Marissa Zhou
# CreatedAt: 10/10/2014

"""Interesting play with Hanoi in Python."""

class Hanoi:
    """
        Class of Hanoi
        Solution for Hanoi Moves Puzzle
        Ideas: BFS + backtrack
    """
    N = 0 # number of discs [1, 8], radius of discs
    K = 0 # number of pegs [3, 5]
    M = 0 # the minimum number of moves to complete the transformation

    def __init__(self, n, k):
        self.N = n
        self.K = k

    def hanoiMove(self):
        pass


#################################################
# classic 3 pegs hanoi                          #
#################################################
    def hanoi(self, s, i, d, n):
        """ classic hanoi solution

        :param s: 
        :type s: char
        :param i: 
        :type i: char
        :param d: 
        :type d: char
        :returns: no return
        """
        if (n > 0):
            hanoi(s, d, i, n-1)
            hanoi(i, s, d, n-1)
