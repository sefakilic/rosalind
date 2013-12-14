# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/gcon/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def gcon():
    recs = read_fasta("rosalind_gcon.txt")
    matrix = matlist.blosum62
    alignments = pairwise2.align.globalds(recs[0][1], recs[1][1], matrix, -5, 0)
    print pairwise2.format_alignment(*alignments[0])


