import networkx as nx
import matplotlib.pyplot as plt

def cc():
    with open("rosalind_cc.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(edge_list)

    print len(nx.connected_components(G))

if __name__ == "__main__":
    cc()
