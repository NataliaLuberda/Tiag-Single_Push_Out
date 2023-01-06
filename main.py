import networkx as nx
from CreativeGraph import Graph
import matplotlib.pyplot as plt
import SinglePushOut


def draw(main_graph, filename):
    options = {
        "font_size": 10,
        "verticalalignment": "top"

    }
    plt.clf()
    plt.title(filename)
    label_stable = nx.get_node_attributes(main_graph, 'label')
    pos = nx.spring_layout(main_graph)
    nx.draw_networkx(main_graph, pos, **options)
    nx.draw_networkx_labels(main_graph, pos, labels=label_stable, font_size=10, verticalalignment="bottom")
    # plt.savefig(filename) # if we want to dave the image
    plt.show()


def start():
    which_example = input('Choose example [1, 2]: ')
    if which_example.isdigit() and int(which_example) in [1, 2]:
        graphs = Graph.from_file("example" + which_example + ".txt")
        start_graph = graphs[0].G
        draw(start_graph, 'start_graph.png')
        transformation_count = int((len(graphs) - 1) / 2)
        index_transformation_arr = [str(i) for i in range(1, transformation_count + 1)]
        which_transformation = int(input('Choose transformation ' + '[' + ','.join(index_transformation_arr) + ']: '))
        left = graphs[which_transformation * 2 - 1].G
        right = graphs[which_transformation * 2].G
        flag_draw_left = input('draw left side of transformation [y/n] :')
        if flag_draw_left == 'y':
            draw(left, 'left_side_transformation.png')
        flag_draw_right = input('draw right side of transformation [y/n] :')
        if flag_draw_right == 'y':
            draw(right, 'right_side_transformation.png')
        transformed_graph = SinglePushOut.spo(left, right, start_graph)
        draw(transformed_graph, 'transformed_graph.png')


if __name__ == "__main__":
    start()

    # przykładowy graf
    # graphs = Graph.from_file("example1.txt")

    # nx.draw(G)
    # labels = ['K', 'L', 'M', 'N']
    # edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    # mainGraph = Graph(labels, edges).G
    # draw(mainGraph, "main_graph")
    # graph = Graph(['K', 'L', 'M', 'N'], [(0, 1), (1, 3), (3, 2), (2, 0)])
    # L = Graph(['K', 'L', 'M'], [(0, 1), (0, 2)])
    # R = Graph(['L', 'M'], [(0, 1)])
    # # Graph1 = Graph(['A', 'B', 'C'], [(0, 1), (1, 2)])
    # transformation = SinglePushOut.spo(L.G, R.G, graph.G)
    #
    # nx.draw(transformation)









