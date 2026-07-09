from random import sample
#this is a python file that generate 2 json file(graph.json and steps.json)
#run_bfs_and_export() will return and save 2 json file 

def random_graph_generator(node_c=20,edge_c=10):
    nodes = [i+1 for i in range(node_c)]
    edges = [tuple(sample(nodes,2)) for i in range(edge_c)]
    return nodes,edges

z = random_graph_generator()
print(z)