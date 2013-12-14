# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/laff/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def laff():
    recs = read_fasta("rosalind_laff.txt")
    matrix = matlist.blosum62
    alignments = pairwise2.align.localds(recs[0][1], recs[1][1], matrix, -11, -1,
                                         one_alignment_only=True)
    best_alignment = alignments[0]

    #print best_alignment
    #print pairwise2.format_alignment(*best_alignment)

    start,end = best_alignment[3:]
    print int(best_alignment[2])
    print best_alignment[0][start:end]
    print best_alignment[1][start:end]




