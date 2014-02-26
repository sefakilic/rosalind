# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/5a/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

DP = {0:0} # DP[x] is the number of coins that changes money.

def _5a():
    with open("rosalind_5a.txt") as f:
        money = int(f.readline())
        denoms = map(int, f.readline().split(','))
        
    for d in denoms:
        DP[d] = 1

    for i in xrange(2, money+1):
        DP[i] = INF
        for d in denoms:
            if i >= d and DP[i-d] + 1 < DP[i]:
                DP[i] = DP[i-d] + 1

    return DP[money]
    



