# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/pcov/
"""

import sys
sys.path.append('../../')
import rosalind_utils

def pcov():
    kmers = [line.strip() for line in open("rosalind_pcov.txt").readlines()]
    edges = dict((kmera, kmerb)
                 for kmera in kmers for kmerb in kmers
                 if kmera[1:] == kmerb[:-1])

    # the de Bruijn graph consists of exactly one simple cycle
    node = edges.keys()[0]
    merged = edges.keys()[0]
    while edges[node] != edges.keys()[0]:
        #print node, edges[node]
        merged += edges[node][-1]
        node = edges[node]
    # get first k characters
    print merged[:len(kmers)]
