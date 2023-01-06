
def spo(left, right, main):

    to_delete = []
    for i, label in enumerate(left.labels):
        if label not in right.labels:
            to_delete.append(label)
    for i in to_delete:
        for j in range(len(main.labels)):
            if i == main.labels[j]:
                main.G.remove_edges_from(list(main.G.edges(j)))
                main.G.remove_node(j)
                break

    new_nodes = []
    for i, label in enumerate(right.labels):
        if label not in left.labels:
            new_nodes.append(label)
    for i in range(len(new_nodes)):
        main.G.add_node(len(main.labels)+i,label=new_nodes[i])

    for i in list(right.G.edges):
        print(i)
        a = right.labels[i[0]]
        b = right.labels[i[1]]
        a1 = 0
        b1 = 0
        for j in range(len(main.labels)):
            if main.labels[j] == a:
                a1 = j
            if main.labels[j] == b:
                b1 = j
        main.G.add_edge(a1,b1)

    return main.G

