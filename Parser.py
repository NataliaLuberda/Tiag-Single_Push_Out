# W powyższym przykładzie zakładamy, że zmienna left_graph zawiera graf lewej strony produkcji,
# a zmienna assignment zawiera przyporządkowanie w postaci stringa.
# Zmienna error_warning jest obiektem aplikacji kivy,
# który jest potrzebny do wyświetlania komunikatów błędów w interfejsie graficznym.


def parse(main_graph, left_graph, przyporządkowanie, error_warning):
    try:
        #Parsuj ciąg przyporządkowania do listy krotek
        assignment_tuples = [tuple(map(int, edge.split(','))) for edge in przyporządkowanie.split('),(')]
    except ValueError:
        error_warning.choice.error_noticed("Invalid assignment format")
        return [], False

    # Przekształć listę krotek w słownik mapujący wierzchołki z lewego grafu na główny graf
    assignment_dict = {vertex_left: vertex_main for vertex_main, vertex_left in assignment_tuples}

    # Sprawdź, czy każdy wierzchołek w lewym grafie jest przypisany do dokładnie jednego wierzchołka w głównym grafie.
    for vertex_left, vertex_main in assignment_dict.items():
        if vertex_left in assignment_dict.values() or vertex_main in assignment_dict.keys():
            error_warning.choice.error_noticed("Each vertex must be assigned to exactly one vertex")
            return [], False

    # Sprawdź, czy liczba wierzchołków przypisana w przyporządkowaniu jest równa liczbie wierzchołków w grafie lewym
    if len(assignment_dict) != left_graph.number_of_nodes():
        error_warning.choice.error_noticed("Assignment incompatible with number of vertices in left graph")
        return [], False

    # Sprawdź, czy wszystkie wierzchołki w przyporządkowaniu istnieją w obu grafach lewej i głównej.
    for vertex_left, vertex_main in assignment_dict.items():
        if not left_graph.has_node(vertex_left):
            error_warning.choice.error_noticed("Invalid assignment (vertex does not exist in left graph)")
            return [], False
        if not main_graph.has_node(vertex_main):
            error_warning.choice.error_noticed("Invalid assignment (vertex does not exist in main graph)")
            return [], False

    # Sprawdź, czy wszystkie etykiety wierzchołków w przyporządkowaniu są zgodne.
    for vertex_left, vertex_main in assignment_dict.items():
        if left_graph.nodes[vertex_left]['label'] != main_graph.nodes[vertex_main]['label']:
            error_warning.choice.error_noticed("Invalid assignment (incompatible vertex labels)")
            return [], False

    # Sprawdź, czy wszystkie etykiety wierzchołków w przypisaniu są zgodne.
    for edge in left_graph.edges:
        if not main_graph.has_edge(assignment_dict[edge[0]], assignment_dict[edge[1]]):
            error_warning.choice.error_noticed("Invalid assignment (edge does not exist in main graph)")
            return [], False

    #Jeżeli wszystko wporządku, zwracam true
    return assignment_tuples, True


def error_handler(error_message,warning):
    warning.choice.error_noticed(error_message)
    return
