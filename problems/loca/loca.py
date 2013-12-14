# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/loca/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def loca():
    recs = read_fasta("rosalind_loca.txt")
    matrix = matlist.pam250
    alignments = pairwise2.align.localds(recs[0][1], recs[1][1], matrix, -5, -5)
    #print pairwise2.format_alignment(*alignments[0])
    start,end = alignments[0][3:]
    print int(alignments[0][2])
    print alignments[0][0][start:end].replace('-','')
    print alignments[0][1][start:end].replace('-','')


