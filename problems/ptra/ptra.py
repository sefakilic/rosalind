# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/ptra/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio.Seq import translate

def ptra():
    with open("rosalind_ptra.txt") as f:
        dna = f.readline().strip()
        prot = f.readline().strip()

    print dna
    print prot

    table = 1
    while translate(dna, table=table, to_stop=True) != prot:
        table += 1

    print table
