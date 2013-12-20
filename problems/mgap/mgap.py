# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/mgap/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import cpairwise2
from Bio import pairwise2

def mgap():
    recs = read_fasta("rosalind_mgap.txt")
    alignments = pairwise2.align.globalms(recs[0][1], recs[1][1], 1, -10**5, -1, -1, score_only=True)
    max_gap = 0
    for alignment in alignments:
        num_gaps = 0
        for i in xrange(len(alignment[0])):
            if alignment[0][i] == '-' or alignment[1][i] == '-':
                num_gaps += 1
        num_gaps = max(num_gaps, max_gap)

    return num_gaps
