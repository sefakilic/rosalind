import networkx as nx
import matplotlib.pyplot as plt

def sq():
    with open("rosalind_sq.txt") as f:
        lines = f.readlines()
        # remove empty lines
        lines = [line for line in lines if line.strip()]

    # Num test cases
    t = int(lines[0])
    del lines[0]
    for i in xrange(t):
        n, e = map(int, lines[0].split())
        edge_list = map(lambda x: map(int, x.strip().split()), lines[1:e+1])
        del lines[:e+1]

        # Create the graph
        G = nx.DiGraph()
        G.add_nodes_from(range(1,n+1))
        for edge in edge_list:
            G.add_edge(edge[0], edge[1])
            G.add_edge(edge[1], edge[0])


        cycles = [c for c in nx.simple_cycles(G) if len(c)==4]
        if cycles:
            print 1,
        else:
            print -1,

    print ""
if __name__ == "__main__":
    sq()
