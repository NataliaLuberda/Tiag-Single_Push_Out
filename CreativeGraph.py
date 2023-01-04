import networkx as nx



class Graph:
    # __init__ - metoda inicjalizująca obiekt klasy.
    # Tworzy graf z podanych w argumencie listy etykiet i listy krawędzi.
    def __init__(self, labels, edges):
        self.labels = labels
        self.G = nx.Graph()
        for i, label in enumerate(labels):
            self.G.add_node(i, label=label)

        for edge in edges:
            start, end = edge
            if 0 <= start < len(self.G.nodes()) and 0 <= end < len(self.G.nodes()):
                self.G.add_edge(start, end)
            else:
                print("ERROR!!!")
                quit()
    #from_file - metoda tworząca listę grafów na podstawie pliku o podanej ścieżce.
    #Każdy graf jest reprezentowany przez obiekt klasy Graph.
    #Jest to metoda klasy, więc nie musisz tworzyć obiektu, aby ją wywołać.
    #Oto przykłąd jak ją wywołać:
    # graphs = Graph.from_file("file.txt")


    @classmethod
    def from_file(cls, filepath):
        # cls to skrót od class,
        # czyli słowo kluczowe w Pythonie oznaczające klasę.
        # W tej konkretnej metodzie cls jest używane jako argument
        # przekazywany do metody, aby wskazać na klasę, do której
        # należy ta metoda.
        graphs = []
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line[0].isdigit():
                    edges = [tuple(map(int, edge.split())) for edge in line.split(";")]
                else:
                    labels = line.split(";")
                    graphs.append(cls(labels, edges))
        return graphs
