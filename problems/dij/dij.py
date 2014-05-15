import networkx as nx
import matplotlib.pyplot as plt

def dij():
    with open("rosalind_dij.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(range(1,n+1))
    G.add_weighted_edges_from(edge_list)

    for n in G.nodes():
        try:
            print nx.dijkstra_path_length(G, 1, n),
        except:
            # node is not reachable
            print -1,
    print ""
    
if __name__ == "__main__":
    dij()
