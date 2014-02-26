# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/3b/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def dist(pat, dna):
    """Distance between pattern and DNA"""
    k = len(pat)
    x = min(hamming_distance(pat, dna[i:i+k]) for i in xrange(len(dna)-k+1))
    return x

def _3b():
    # read input
    with open("rosalind_3b.txt") as f:
        k = int(f.readline())
        seqs = [seq.strip() for seq in f.readlines()]

    dists = {}
    # For each kmer, find the distance to each sequence
    for kmer in map(lambda x: "".join(x), product("ACTG", repeat=k)):
        dists[kmer] = max(dist(kmer, dna) for dna in seqs)

    # Return any element of the following list is enough
    print [''.join(kmer) for kmer in dists if (dists[kmer] == min(dists.values()))]

