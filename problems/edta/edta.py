# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/edta/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *

def edta():
    recs = read_fasta("rosalind_edta.txt")
    seqa,seqb = recs[0][1], recs[1][1]
    C = edit_distance_helper(seqa, seqb)
    print edit_distance(seqa,seqb)
    print '\n'.join(edit_distance_backtrack(C, seqa, seqb))

