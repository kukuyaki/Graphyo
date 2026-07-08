import networkx as nx
import matplotlib.pyplot as plt
from early_work.graph_input import test,translation_tool,random_gene
#https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html



def show_direct_pic(nodes,edge,graphType="direct weight"):
    G = nx.DiGraph()  # DiGraph為有向圖, Graph為無向
    G.add_nodes_from(nodes)
    G.add_edges_from([i[:2] for i in edge])
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return 0


def show_weight_direct_pic(edge):
    G = nx.DiGraph()
    for a,b,w in edge:
        G.add_edge(a, b, weight=w)
    

    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
    print(pos)
    for i in pos.values():
        print(i)
    edge_labels = nx.get_edge_attributes(G, "weight")
    eAll = [(u, v) for (u, v, d) in G.edges(data=True) ]

    # draw shape
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=eAll)
    
    # draw labels
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    return 0

def pos_f():
    nodes, edge = random_gene()
    unique_nodes = list(set([n for e in edge for n in e[:2]]))
    posw = {old_node: chr(65 + i) for i, old_node in enumerate(unique_nodes)}
    n_edge = [[posw[a], posw[b], w] for a, b, w in edge]
    G = nx.DiGraph()
    big_n = int(max([i[2] for i in n_edge])*1.2)+1
    for a, b, w in n_edge:
        G.add_edge(a, b, weight=big_n-w)
    pos_init = nx.spring_layout(G, k=0.8, iterations=50,  seed=42)
    pos = nx.kamada_kawai_layout(G, pos=pos_init)
    posn = {node: [float(coords[0]), float(coords[1]), 0] for node, coords in pos.items()}
    print(posn)
    print(n_edge)
    return posn, n_edge
if __name__ == "__main__":
    # nodes,edge = gt.translation_tool()
    nodes,edge = gt.test()
    pos_f(edge)
    # show_direct_pic(nodes,edge)
    # show_weight_direct_pic(edge)


#First, graph_input, get nodes and edge and weight
#Second, according to the info you get, use networkx to get x and y of node position
#Third, matplotlib to show graph

#this is graph show method, not even include path finding algorithm