# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/filt/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def filt():
    with open("rosalind_filt.txt") as f:
        q, p = map(int, f.readline().split())
        fastq = f.read()
    with open("foo.fastq", 'w') as f:
        f.write(fastq)

    num_filtered = 0
    recs = SeqIO.parse("foo.fastq", "fastq")
    for rec in recs:
        quals = rec.letter_annotations["phred_quality"]
        # find num of bases above quality threshold
        nb = sum([1 if b >= q else 0 for b in quals])
        if nb < len(quals) * p / 100.0:
            num_filtered += 1

    print num_filtered

if __name__ == '__main__':
    filt()

