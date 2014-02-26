# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/5c/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

import sys
sys.setrecursionlimit(10000)

def _5c():
    with open("rosalind_5c.txt") as f:
        seqa = f.readline().strip()
        seqb = f.readline().strip()

    # Find the longest common subsequence
    C = lcsq(seqa, seqb)
    return lcsq_backtrack(C, seqa, seqb, len(seqa), len(seqb))




