import networkx as nx
import matplotlib.pyplot as plt

# Create a graph to simulate the ant colony network
G = nx.Graph()
edges = [(1, 2, 5), (2, 3, 10), (1, 3, 15), (3, 4, 5), (2, 4, 20)]
G.add_weighted_edges_from(edges)

# Draw the graph
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=12)
edge_labels = {(u, v): f"{w}" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Ant Colony Optimization - Graph Representation")
plt.show()