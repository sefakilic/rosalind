# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1a/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

from collections import defaultdict

def _1a():
    with open("rosalind_1a.txt") as f:
        seq = f.readline().strip()
        k = int(f.readline())

        
    d = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        d[seq[i:i+k]] += 1
    max_occ = max(d.values())
    for k,v in d.items():
        if v == max_occ:
            print k,
    print ""
        

