# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/4a/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _4a():
    with open("rosalind_4a.txt") as f:
        k = int(f.readline())
        seq = f.readline().strip()

    # return all k-mers in lexicographic order
    print '\n'.join(sorted(seq[i:i+k] for i in xrange(len(seq)-k+1)))
