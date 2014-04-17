# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1g/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
from collections import defaultdict
from itertools import product

def mismatch(seqa, seqb):
    return sum([1 if a!=b else 0 for a,b in zip(seqa,seqb)])

def pat_similar(pat, d, alph="ACTG"):
    """Return all strings that are at most d mismatch distant from pat"""
    if d==0:
        return set([pat])
    ret = set()
    for i in xrange(len(pat)):
        for c in alph:
            s = pat_similar(pat[:i] + c + pat[i+1:], d-1, alph)
            ret = ret.union(s)
    return ret

def _1g():
    with open("rosalind_1g.txt") as f:
        seq = f.readline().strip()
        k, d = map(int, f.readline().split())

    dic = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        dic[seq[i:i+k]] += 1

    mm_dic = defaultdict(int)
    for k,v in dic.items():
        for mm in pat_similar(k, d):
            mm_dic[mm] += v
        sys.stdout.flush()

    print mm_dic

    max_occ = max(mm_dic.values())
    for k,v in mm_dic.items():
        if v == max_occ:
            print k,

    print ""

        
                
        
        
