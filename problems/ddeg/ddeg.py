import networkx as nx
import matplotlib.pyplot as plt

def ddeg():
    with open("rosalind_ddeg.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(edge_list)

    for node in G.nodes():
        print sum([G.degree(n) for n in G.neighbors(node)]),
    print ""

    
if __name__ == "__main__":
    ddeg()
