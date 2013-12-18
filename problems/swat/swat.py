# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/swat/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from Bio import Entrez
Entrez.email = "sefa1@umbc.edu"

def dl_seq(id):
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record.seq.tostring()

def swat():
    genbank_ids = open("rosalind_swat.txt").read().split()
    seqa = dl_seq(genbank_ids[0])
    seqb = dl_seq(genbank_ids[1])
    with open("seqa.faa", 'w') as f:
        f.write('>seqa\n%s\n' % seqa)
    with open("seqb.faa", 'w') as f:
        f.write('>seqb\n%s\n' % seqb)
    swat_cline = "water -asequence ./seqa.faa -bsequence ./seqb.faa -gapopen 10 -gapextend 1 -outfile swat.txt"

    import os
    os.system(swat_cline)
    



