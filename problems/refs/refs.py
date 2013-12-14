# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/refs/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import Entrez
Entrez.email = "sefa1@umbc.edu"

def refs():
    sp, a, b, dat = open("rosalind_refs.txt").read().strip().split('\n')
    term = '%s[ORGN] AND %s:%s[PDAT] AND %s:%s[SLEN] AND srcdb_refseq[PROP]' % \
           (sp, "1000", dat, a, b)
    handle = Entrez.esearch(db="nuccore", term=term)
    record = Entrez.read(handle)
    handle.close()
    return record
