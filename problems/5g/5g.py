# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/edit/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *

# edit distance is same as the length of longest common subsequence
def edit():
    with open("rosalind_5g.txt") as f:
        seqa = f.readline().strip()
        seqb = f.readline().strip()
    return edit_distance(seqa, seqb)
