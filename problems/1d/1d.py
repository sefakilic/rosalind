# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1d/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

from collections import defaultdict

def _1d():
    with open("rosalind_1d.txt") as f:
        seq = f.readline().strip()
        k, L, t = map(int, f.readline().split())

    clumps = set()

    for i in xrange(len(seq)-L+1):
        d = defaultdict(int)
        for j in xrange(L-k+1):
            d[seq[i+j:i+j+k]] += 1
        for kmer,cnt in d.items():
            if cnt >= t:
                clumps.add(kmer)

    for c in clumps:
        print c,
    print ""
