
def spo(left, right, m):

    to_delete = []
    for i, label in enumerate(left.labels):
        if label not in right.labels:
            to_delete.append(label)
    for i in to_delete:
        for j in range(len(m.labels)):
            if i == m.labels[j]:
                m.G.remove_edges_from(list(m.G.edges(j)))
                m.G.remove_node(j)
                break

    new_nodes = []
    new_labels = []
    for i, label in enumerate(right.labels):
        if label not in left.labels:
            new_nodes.append(label)
    for i in range(len(new_nodes)):
        new_labels.append(new_nodes[i])
        m.G.add_node(len(m.labels)+i,label=new_nodes[i])

    m.labels = m.labels + new_labels

    for i in list(right.G.edges):
        a = right.labels[i[0]]
        b = right.labels[i[1]]

        if a in m.labels and b in m.labels:
            a1 = 0
            b1 = 0
            for j in range(len(m.labels)):
                if m.labels[j] == a:
                    a1 = j
                if m.labels[j] == b:
                    b1 = j
            m.G.add_edge(a1,b1)



    return m.G

