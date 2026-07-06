#docker run --rm -it graphyo-env

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

    edge.sort(key=lambda x:(x[0], x[1]))
    for i in edge:
        print(i)
    print(edge)

if __name__ == "__main__":
    translation_tool()

