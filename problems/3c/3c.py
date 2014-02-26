# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/3c/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _3c():
    # read input
    with open("rosalind_3c.txt") as f:
        seq = f.readline().strip()
        k = int(f.readline())
        # read the matrix
        matrix = []
        for i in xrange(k):
            nums = map(float, f.readline().split())
            matrix.append(dict(zip("ACGT", nums)))
            
    # find the most-probable kmer in the seq
    best_score = 0
    best_seq = seq[:k]
    for i in xrange(len(seq)-k+1):
        text = seq[i:i+k]
        tmp_score = sum(matrix[j][text[j]] for j in xrange(k))
        if tmp_score > best_score:
            best_score = tmp_score
            best_seq  = text

    print best_seq
        
            
