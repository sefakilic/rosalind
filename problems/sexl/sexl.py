# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/sexl/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *


def sexl():
    ps = map(float, open("rosalind_sexl.txt").read().split())
    print " ".join(map(str, [2*p*(1-p) for p in ps]))

