# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/conv/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
from collections import Counter

def conv():
    with open("rosalind_conv.txt") as f:
        s = map(float, f.readline().split())
        t = map(float, f.readline().split())

    spec_conv = [round(a-b, 5) for a in s for b in t]

    x = Counter(spec_conv).most_common(1)
    print x[0][1]
    print x[0][0]
    
