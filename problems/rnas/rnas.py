# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/rnas/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

memo = {}
def helper(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    if seq in memo:
        return memo[seq]

    memo[seq] = helper(seq[1:])
    for i in xrange(4,len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
            (seq[0] == 'U' and seq[i] == 'A') or
            (seq[0] == 'C' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'C') or
            (seq[0] == 'U' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'U')):
            memo[seq] += helper(seq[1:i]) * helper(seq[i+1:])
    return memo[seq]

def rnas():
    seq = open("rosalind_rnas.txt").read().strip()
    print helper(seq)
    
