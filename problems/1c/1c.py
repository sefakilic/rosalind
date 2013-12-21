# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1c/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def _1c():
    with open("rosalind_1c.txt") as f:
        pat = f.readline().strip()
        seq = f.readline().strip()

    index = seq.find(pat)
    while index >= 0:
        print index,
        index = seq.find(pat, index+1)
    print ""
        
    
