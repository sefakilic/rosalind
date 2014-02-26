# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/gasm/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
import networkx
import pylab

def gasm():
    lines = map(lambda x: x.strip(), open("rosalind_gasm.txt").readlines())
    seqs = set([line for line in lines] +
               [reverse_complement(line) for line in lines])

    n = len(list(seqs)[0]) # length of reads

    for k in range(n-1, 1, -1):
        # construct the de Bruijn graph
        print k
        tmp_seqs = set()
        for seq in seqs:
            for i in xrange(n-k):
                tmp_seqs.add(seq[i:i+k+1])
        print "constructing graph"
        G = networkx.DiGraph()
        for seq in tmp_seqs:
            a = seq[:k]
            b = seq[-k:]
            if a not in G.nodes():
                G.add_node(a)
            if b not in G.nodes():
                G.add_node(b)
            G.add_edge(a,b)
        print len(G.nodes()), len(G.edges())
        #networkx.draw(G)
        #pylab.show()
        print "searching for cycles"
        cycles = networkx.simple_cycles(G)
        if len(cycles) == 2:
            print "found cycles"
            print cycles
            super_str = cycles[0][0]
            for elm in cycles[0][1:-k]:
                super_str = super_str + elm[-1]
            print super_str
        

    return G


