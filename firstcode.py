import networkx as nx
import matplotlib.pyplot as plt
import graph_input as gt
G = nx.Graph()  # DiGraph為有向圖, Graph為無向

nodes,edge = gt.translation_tool()

G.add_nodes_from(nodes)
G.add_edges_from(edge)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()