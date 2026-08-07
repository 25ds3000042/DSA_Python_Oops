#Constructor
class Graph:
    def __init__(self):
        self.graph = {}
        
#  Adding Vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
# Adding edges
    def add_edge(self,v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
        
    def print_graph(self):
        for vertex in self.graph:
            print(vertex,"->", self.graph[vertex])
        
        
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

g.print_graph()