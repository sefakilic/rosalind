# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/2b/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _2b():
    # read input
    with open("rosalind_2b.txt") as f:
        dnaseq = f.readline().strip()
        aaseq = f.readline().strip()

    # search substrings of dnaseq to check if any of them translates to aaseq
    for i in xrange(0, len(dnaseq)-len(aaseq)*3+1):
        seq = dnaseq[i:i+len(aaseq)*3]
        if (translate(transcribe(seq)) == aaseq or
            translate(transcribe(reverse_complement(seq))) == aaseq):
            print seq




