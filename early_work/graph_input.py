#docker run --rm -it graphyo-env
import random.random
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

    return nodes, edge
if __name__ == "__main__":
    translation_tool()

