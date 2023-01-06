import networkx as nx


def spo(left, right, main):

    to_delete = []
    for i in list(left.nodes):
        main.remove_edges_from(left.edges(i))
        if i not in list(right.nodes):
            to_delete.append(i)
    for i in to_delete:
        main.remove_node(i)

    new_nodes = []
    for i in list(right.nodes):
        if i not in list(left.nodes):
            new_nodes.append(i)
    for i in new_nodes:
        main.add_node(i)
    for i in list(right.nodes):
        main.add_edges_from(right.edges(i))
    print(list(main.nodes))
    return main
