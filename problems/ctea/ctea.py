# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/ctea/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *

lookup = {} # loopup values for fast computation

def num_optimal_alignments(C, s, t, i, j):
    if i==0 or j == 0:
        return 1
    if (i,j) not in lookup:
        total_ways = 0
        if C[i][j] == C[i-1][j] + 1:
            total_ways += num_optimal_alignments(C, s, t, i-1, j)
        if C[i][j] == C[i][j-1] + 1: 
            total_ways += num_optimal_alignments(C, s, t, i, j-1)
        if C[i][j] == C[i-1][j-1] and s[i-1] == t[j-1]:
            total_ways += num_optimal_alignments(C, s, t, i-1, j-1)
        if C[i][j] == C[i-1][j-1] + 1 and s[i-1] != t[j-1]:
            total_ways += num_optimal_alignments(C, s, t, i-1, j-1)

        assert total_ways > 0
        
        lookup[(i,j)] =  total_ways % (2**27 - 1)

    return lookup[(i,j)]

def ctea():
    recs = read_fasta("rosalind_ctea.txt")
    seqa, seqb = recs[0][1], recs[1][1]
    C = edit_distance_helper(seqa, seqb)
    #for r in C: print r
    #print seqa
    #print seqb
    print num_optimal_alignments(C, seqa, seqb, len(seqa), len(seqb))
