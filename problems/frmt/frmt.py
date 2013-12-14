# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/frmt/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *

from Bio import Entrez
Entrez.email = "sefa1@umbc.edu"

def frmt():
    ids = open("rosalind_frmt.txt").read().split()
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()

    shortest_rec = min(records, key=lambda rec: len(rec.seq))
    print shortest_rec.format("fasta")




