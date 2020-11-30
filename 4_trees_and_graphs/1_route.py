from graph import Graph, Node

def route(graph, node, data):
    for child in node.children:
        if graph.nodes[child].data == data:
            return True
        return route(graph, graph.nodes[child], data)
    return False

def test_simple():
    graph = Graph()
    graph.nodes.append(Node(5))
    graph.nodes.append(Node(8))
    graph.nodes.append(Node(9))
    graph.nodes.append(Node(1))
    graph.nodes.append(Node(4))

    graph.nodes[0].children = [1, 2]
    graph.nodes[1].children = [3, 4]

    assert route(graph, graph.nodes[0], 4)