import networkx as nx
import matplotlib.pyplot as plt
import graph_input as gt
#https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html



def show_one_pic(nodes,edge,graphType="direct weight"):
    G = nx.DiGraph()  # DiGraph為有向圖, Graph為無向
    G.add_nodes_from(nodes)
    G.add_edges_from(edge)
    nx.draw(G, with_labels=True, font_weight='bold')

    pos = nx.spring_layout(G,seed=7)
    nx.draw_networkx_nodes(G,pos,node_size=700)
    nx.draw_networkx_edges()
    nx.draw_networkx_labels()
    plt.show()
    return 0

if __name__ == "__main__":
    nodes,edge = gt.translation_tool()
    show_one_pic(nodes,edge)


#First, graph_input, get nodes and edge and weight
#Second, according to the info you get, use networkx to get x and y of node position
#Third, matplotlib to show graph

#this is graph show method, not even include path finding algorithm