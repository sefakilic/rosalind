# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/afrq/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

def afrq():
    nums = map(float, open("rosalind_afrq.txt").read().split())
    print " ".join(map(str, [1-(1-sqrt(num))**2 for num in nums]))
    

    

