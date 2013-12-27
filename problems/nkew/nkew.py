# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/nkew/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *

import networkx, pylab

def nkew():
    with open("rosalind_nkew.txt") as f:
        lines = map(lambda l: l.strip(), f.readlines())
        lines = [line for line in lines if line]

    for i in xrange(len(lines)/2):
        handle = StringIO(lines[2*i])
        tree = Phylo.read(handle, "newick")
        names = lines[2*i+1].split()

        t =  Phylo.to_networkx(tree)
        print t.edges()
        # create weighted tree
        wt = networkx.Graph()
        for node in t.nodes():
            wt.add_node(node)
        for edge in t.edges():
            wt.add_edge(edge[0], edge[1], weight=edge[0].branch_length)

        
        na = [node for node in wt.nodes() if node.name == names[0]][0]
        nb = [node for node in wt.nodes() if node.name == names[1]][0]

        print wt.edges(data=True)

        #path_len = sum(node.branch_length if node.name else 0 for node in networkx.shortest_path(t, na, nb))
        #print path_len,
        print networkx.shortest_path_length(wt, na, nb, 'weight')

    print ""
