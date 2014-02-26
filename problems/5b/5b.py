# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/5b/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
INF = 10**10

def south_or_east(i, j, south, east):
    """THe length of longest path in a rectangular grid, where down and east are
    two matrices, costs of moving south and east at any position,
    respectively."""""
    if i==0 and j==0:
        return 0
    x = 0
    y = 0
    if i > 0:
        x = south_or_east(i-1, j, south, east) + south[i-1][j]
    if j > 0:
        y = south_or_east(i, j-1, south, east) + east[i][j-1]
    return max(x,y)
    
def _5b():
    with open("rosalind_5b.txt") as f:
        n, m = map(int, f.readline().split())
        # matrix of costs to move south at any position
        south = []
        for i in xrange(n):
            south.append(map(int, f.readline().split()))
        # read line with a dash
        f.readline()
        # matrix of costs to move east at any position
        east = []
        for i in xrange(n+1):
            east.append(map(int, f.readline().split()))
            
    return south_or_east(n, m, south, east)
