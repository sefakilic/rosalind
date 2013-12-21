# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/1h/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

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

def _1h():
    with open("rosalind_1h.txt") as f:
        seq = f.readline().strip()
        k, d = map(int, f.readline().split())

    dic = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        dic[seq[i:i+k]] += 1
        dic[reverse_complement(seq[i:i+k])] += 1

    mm_dic = defaultdict(int)
    for k,v in dic.items():
        for mm in pat_similar(k, d):
            mm_dic[mm] += v
        sys.stdout.flush()

    max_occ = max(mm_dic.values())
    for k,v in mm_dic.items():
        if v == max_occ:
            print k,

    print ""
