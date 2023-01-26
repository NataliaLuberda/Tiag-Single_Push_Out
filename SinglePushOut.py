
def spo(left, right, m):

    to_delete = []
    for i, label in enumerate(left.labels):
        if i not in right.G.nodes:
            to_delete.append([label,i])
    for i in to_delete:
        for j in range(len(m.labels)):
            if i[0] == m.labels[j]:
                m.G.remove_edges_from(list(m.G.edges(j)))
                m.G.remove_node(j)
                break
    for i in to_delete:
        m.labels[i[1]] = -1

    new_nodes = []
    new_labels = []
    for i, label in enumerate(right.labels):
        if i not in left.G.nodes:
            new_nodes.append([label,i])
    for i in range(len(new_nodes)):
        new_labels.append(new_nodes[i][0])
        m.G.add_node(len(m.labels)+i,label=new_nodes[i][0])

    m.labels = m.labels + new_labels

    for i in list(left.G.edges):
        a = left.labels[i[0]]
        b = left.labels[i[1]]

        if a in m.labels and b in m.labels and a != -1 and b != -1:
            a1 = 0
            b1 = 0
            for j in range(len(m.labels)):
                if m.labels[j] == a:
                    a1 = j
                if m.labels[j] == b:
                    b1 = j
            if (a1,b1) in m.G.edges:
                m.G.remove_edge(a1,b1)

    for i in list(right.G.edges):
        if len(list(left.G.nodes)) >= len(list(right.G.nodes)):
            a = left.labels[i[0]]
            b = left.labels[i[1]]
        else:
            a = right.labels[i[0]]
            b = right.labels[i[1]]

        if a in m.labels and b in m.labels and a != -1 and b != -1:
            a1 = 0
            b1 = 0
            for j in range(len(m.labels)):
                if m.labels[j] == a:
                    a1 = j
                if m.labels[j] == b:
                    b1 = j
            m.G.add_edge(a1,b1)

    return m.G

