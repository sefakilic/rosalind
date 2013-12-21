# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1e/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _1e():
    seq = open("rosalind_1e.txt").read().strip()
    min_skew_sc = 0
    min_skew_ints = [0]
    cur_skew_sc = 0
    for i in xrange(len(seq)):
        if seq[i] == "G":
            cur_skew_sc += 1
        elif seq[i] == "C":
            cur_skew_sc -= 1

        if cur_skew_sc == min_skew_sc:
            min_skew_ints.append(i+1)

        if cur_skew_sc < min_skew_sc:
            min_skew_sc = cur_skew_sc
            min_skew_ints = [i+1]

    print " ".join(map(str, min_skew_ints))
            



