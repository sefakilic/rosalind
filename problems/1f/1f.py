# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1f/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def mismatch(seqa, seqb):
    return sum([1 if a!=b else 0 for a,b in zip(seqa,seqb)])

def _1f():
    with open("rosalind_1f.txt") as f:
        pat = f.readline().strip()
        seq = f.readline().strip()
        d = int(f.readline())

    for i in xrange(len(seq)-len(pat)+1):
        if mismatch(seq[i:i+len(pat)], pat) <= d:
            print i,

    print ""
            
