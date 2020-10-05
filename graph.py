class Vertex:
    def __init__(self, name):
        self.edges = []
        self.name = name

    def connect(self, targetVertex, distance):
        connection = Edge(distance, self, targetVertex)
        self.edges.append(connection)


class Edge:
    def __init__(self, distance, originVertex, targetVertex):
        self.distance = distance
        self.originVertex = originVertex
        self.targetVertex = targetVertex


def shortestRoute(originVertex, targetVertex):
    if originVertex == targetVertex:
        return 0
    else:
        if len(originVertex.edges) > 0:
            distances = []
            for edge in originVertex.edges:
                distances.append(shortestRoute(edge.targetVertex, targetVertex) + edge.distance)
            return min(distances)
        else:
            return 0

a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")

a.connect(b, 300)
a.connect(c, 90)
a.connect(d, 300)
b.connect(d, 100)
b.connect(e, 400)
c.connect(d, 200)
c.connect(e, 500)
d.connect(e, 100)

print(shortestRoute(a, d))
