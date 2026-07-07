import networkx as nx
import matplotlib.pyplot as plt
import graph_input as gt
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
if __name__ == "__main__":
    # nodes,edge = gt.translation_tool()
    nodes,edge = gt.test()
    show_direct_pic(nodes,edge)
    show_weight_direct_pic(edge)


#First, graph_input, get nodes and edge and weight
#Second, according to the info you get, use networkx to get x and y of node position
#Third, matplotlib to show graph

#this is graph show method, not even include path finding algorithm