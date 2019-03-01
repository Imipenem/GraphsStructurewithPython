import click
from node import Node
from graph import Graph


# @click.command()
# @click.option('--ide', default='DummyID')
# @click.option('--node', type=Node)

@click.command()
@click.option('--name', default='DummyName', prompt="Enter a graphs name")
def main(name):
    node1 = Node(1, 3)
    node2 = Node(12, 13)
    node3 = Node(22, 100)
    graph = Graph()
    graph.add_node(node1, node2, node3)
    print('Graphs name is {}'.format(name))
    graph.connect(node1, node2)
    graph.connect(node2, node3)
    for edge in graph.allEdges:
        edge.__str__()
    graph.disconnect(node1, node2)
    print('After removal:')
    for edge in graph.allEdges:
        edge.__str__()


if __name__ == "__main__":
    main()
