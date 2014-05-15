import networkx as nx
import matplotlib.pyplot as plt

def bfs():
    with open("rosalind_bfs.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(edge_list)

    dists = nx.single_source_shortest_path_length(G, 1)
    for n in G.nodes():
        print dists.get(n, -1),
    print ""
    
if __name__ == "__main__":
    bfs()
