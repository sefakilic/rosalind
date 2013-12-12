# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/dbru/
"""

import sys
sys.path.append('../../')
import rosalind_utils

def dbru():
    S = [line.strip() for line in open("rosalind_dbru.txt").readlines()]
    S_revcomp = [rosalind_utils.reverse_complement(s) for s in S]
    # build the De Bruijn graph
    edges = set((s[:-1], s[1:]) for s in S).\
            union(set((s[:-1], s[1:]) for s in S_revcomp))
    for e in edges:
        print '(%s, %s)' % (e[0], e[1])

    

