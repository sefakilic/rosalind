# -*- coding: utf-8 -*- 

"""
see http://rosalind.info/problems/sset/
"""

import sys
sys.path.append('../../')
import rosalind_utils

def sset():
    n = int(open("rosalind_sset.txt").read())
    return 2**n % 10**6
