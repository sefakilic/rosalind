# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/rear/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
import Queue

def swap(lst, i, j):
    sublst = lst[i:j+1]
    sublst.reverse()
    lst = lst[:i] + sublst + lst[j+1:]
    return lst

def helper(s,t):
    """Given two permutations, return the reversal distance"""
    queue = Queue.Queue()
    visited = set()
    
    queue.put((s,0))
    while not queue.empty():
        x,d = queue.get()
        visited.add(tuple(x))
        if x == t:
            return d
        for i in xrange(len(x)):
            for j in xrange(i+1, len(x)):
                tmp = swap(x[:], i, j)
                if tuple(tmp) not in visited:
                    queue.put((tmp, d+1))
    print "shouldn't be here"
                
def rear():
    with open("rosalind_rear.txt") as f:
        lines = map(lambda x: x.strip(), f.readlines())
        lines = [line for line in lines if line.strip()]

    for i in xrange(len(lines)/2):
        s = map(int, lines[2*i].split())
        t = map(int, lines[2*i+1].split())
        # map list of numbers to string (list of chars) for memory efficency
        cs = "".join(chr(ord('a') + i) for i in s)
        ts = "".join(chr(ord('a') + i) for i in t)
        print cs
        print ts
        print helper(s,t)

        
