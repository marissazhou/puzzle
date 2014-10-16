#!/usr/bin/env python
# HanoiMoves.py
# Author: Lijuan Marissa Zhou
# CreatedAt: 10/10/2014

"""Interesting play with Pascals Triangle Problem in Python."""

class PascalsTriangle:
    """
        Class of PascalsTriangle
    """
    def __init__(self):
        self.data = []

    def generate(self, n):
        """
        Given numRows, generate the first numRows of Pascal's triangle.

        :param  n: number of layers of pascal's triangle
        :type   n: number 
        :return: a list of lists of integers
        :rtype: list 
        """
        if (n < 0):
            return None
        if (n == 0):
            return [] 
        self.data = [[1]]
        for i in xrange(1, n):
            rownum = i + 1
            rowi = [1] + [0]*(rownum-2)+[1]
            mid = rownum/2 + rownum%2
            for j in xrange(1, mid):
                val = self.data[i-1][j-1] + self.data[i-1][j]
                rowi[j] = val
                rowi[rownum-j-1] = val
            self.data.append(rowi)
        return self.data

    def printData(self):
        """
            print data
        """
        print self.data

#################################################
# test                                          # 
#################################################

if __name__ == "__main__":
    pt = PascalsTriangle()
    pt.generate(5)
    pt.printData()
