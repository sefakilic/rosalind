# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1b/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _1b():
    seq = open("rosalind_1b.txt").readline()
    print reverse_complement(seq)

