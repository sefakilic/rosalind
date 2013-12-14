# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/gaff/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def gaff():
    recs = read_fasta("rosalind_gaff.txt")
    matrix = matlist.blosum62
    alignments = pairwise2.align.globalds(recs[0][1], recs[1][1], matrix, -11, -1)
    best_alignment = alignments[0]
    
    #print pairwise2.format_alignment(*best_alignment)

    print int(best_alignment[2])
    print best_alignment[0]
    print best_alignment[1]




