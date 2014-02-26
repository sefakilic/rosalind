# -*- coding: utf-8 -*- 

"""
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
from collections import defaultdict
from itertools import product

def pat_similar(pat, d, alph="ACTG"):
    """Return all strings that are at most d mismatch distant from pat"""
    if d==0:
        return set([pat])
    ret = set()
    for i in xrange(len(pat)):
        for c in alph:
            s = pat_similar(pat[:i] + c + pat[i+1:], d-1, alph)
            ret = ret.union(s)
    return ret


def _3a():
    # read input
    with open("rosalind_3a.txt") as f:
        k, d = map(int, f.readline().split())
        seqs = [seq.strip() for seq in f.readlines()]

    # If pattern itself or its neighbor upto d mismatch occurs in all Dna
    cnts = defaultdict(int)
    for kmer in map(lambda x: ''.join(x), product('ACTG', repeat=k)):
        if all(any(pkmer in seq for pkmer in pat_similar(kmer, d)) for seq in seqs):
            cnts[kmer] += 1
        
    print ' '.join(kmer for kmer in cnts.keys() if cnts[kmer]==max(cnts.values()))
    return cnts
        
