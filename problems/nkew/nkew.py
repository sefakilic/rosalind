# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/nkew/
"""

from math import *
import sys
sys.path.append('../../')
from rosalind_utils import *
import StringIO
import networkx
import matplotlib.pyplot as plt
from Bio import Phylo

def nkew():
    with open("rosalind_nkew.txt") as f:
        lines = map(lambda l: l.strip(), f.readlines())
        lines = [line for line in lines if line]

    for i in xrange(len(lines)/2):
        handle = StringIO.StringIO(lines[2*i])
        tree = Phylo.read(handle, "newick")
        names = lines[2*i+1].split()

        t =  Phylo.to_networkx(tree)
        # create weighted tree
        wt = networkx.Graph()
        for node in t.nodes():
            wt.add_node(node)
        for key,vals in t.edge.items():
            for val in vals:
                wt.add_edge(key, val, weight=vals[val]['weight'])

        #pos = networkx.spring_layout(wt)
        #networkx.draw(wt, pos)
        #networkx.draw_networkx_edge_labels(wt, pos)
        #plt.show()
        
        na = [node for node in wt.nodes() if node.name == names[0]][0]
        nb = [node for node in wt.nodes() if node.name == names[1]][0]

        print int(networkx.shortest_path_length(wt, na, nb, 'weight')),
    print ""


if __name__ == "__main__":
    nkew()
