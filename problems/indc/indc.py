# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/indc/
"""

import sys
sys.path.append('../../')
from rosalind_utils import *
from math import *

def binom(n, k, p):
    # probability of obtaining k heads
    return choose(n,k) * p**k * (1-p)**(n-k)

def indc():
    n = int(open("rosalind_indc.txt").read())
    #n = 5
    p = 0.5
    for k in xrange(1, 2*n+1):
        print log(sum(binom(2*n, kk, p) for kk in range(k, 2*n+1)), 10),
    print ""
    

