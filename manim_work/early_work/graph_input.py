#docker run --rm -it graphyo-env
from random import randint,choice
#input node and edge
#test node and edge
#random node and edge

def translation_tool():
    x = 1
    edge = []
    print("Enter edge\n eg. first_node second_node weight\n eg.:1 2 3\nit mean node 1 to node 2 weight 3.")
    while x:
        try:
            new_edge = input(":").split()
            if new_edge == ['0']:
                break
            x = list(map(int,new_edge))  
        except:
            print("Unmatch syntax, do it again.")
            continue
        edge.append(x)

    nodes = set()
    for i in edge:
        nodes.add(i[0])
        nodes.add(i[1])
    edge.sort(key=lambda x:(x[0], x[1]))
    print("*"*20)
    for i in edge:
        print(i)
    print(f"{edge=}")
    print(f"{nodes =}")
    return nodes, edge

def test():
    edge = [[1,2,3],[1,3,3],[1,8,3],[4,2,3],[1,1,3],[1,9,3],[10,2,3],[16,23,10]]
    nodes = set()
    for i in edge:
        nodes.add(i[0])
        nodes.add(i[1])
    edge.sort(key=lambda x:(x[0], x[1]))

    print("*"*20)
    for i in edge:
        print(i)
    print(f"{edge=}")
    print(f"{nodes =}")
    return nodes, edge
def random_gene():
    node_n_min = 5
    node_n_max = 20
    weight_min = 10
    weight_max = 30
    edge_n_max = 20
    edge = [[1,2,3],[1,3,3],[1,8,3],[4,2,3],[1,1,3],[1,9,3],[10,2,3],[16,23,10]]
    possible_node = [i for i in range(1,randint(node_n_min,node_n_max))]
    edge = [[choice(possible_node),choice(possible_node),randint(weight_min,weight_max)] for _ in range(edge_n_max)]
    edge = [i for i in edge if i[0] != i[1]]

    nodes = set()
    for i in edge:
        nodes.add(i[0])
        nodes.add(i[1])
    edge.sort(key=lambda x:(x[0], x[1]))

    print("*"*20)
    for i in edge:
        print(i)
    print(f"{edge=}")
    print(f"{nodes =}")
    return nodes, edge
if __name__ == "__main__":
    translation_tool()

