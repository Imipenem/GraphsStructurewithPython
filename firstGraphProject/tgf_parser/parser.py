from firstGraphProject.graph_model.graph import Graph
from firstGraphProject.node.node import Node


class Parser:
    """
        A class used to parse a graph from a TGF-File

        Attributes
        ----------

        Methods
        -------
        read_nodes(node_line=str, graph = Graph)
            This method reads one line representing a node

        parse_tgf_file(graph = Graph)
            This method parses the whole TGF-file and creates a graph according to the file

    """

    @staticmethod
    def read_nodes(node_line, graph: Graph):
        """
        This method gets one string representing a node and create a new node.

        The common format is: [identifier] [value] (without the brackets)

                Parameters
                ----------
               node_line : str
                    this string represents a node consisting of the identifier followed by the value separated by space
                graph : Graph
                    this is the fundamental graph to be parsed from the TGF-file
        """
        node_line_splitted = node_line.split()
        new_node = Node(node_line_splitted[0], node_line_splitted[1])
        graph.add_node(new_node)

    @staticmethod
    def parse_tgf_file(graph: Graph):
        """
        This method parses the whole file to create nodes and connect them.
        The common format for the nodes can be found at the read_nodes() docstring.

        Nodes and Edges are separated by a #. When # is reached, the (but possibly there will be no connections at all)
        the read_edges() will be invoked.
        Edge Format: [identifier of source_node] [identifier of target_node]
        TODO: read_edges()!!!!

                Parameters
                ----------
                node_line : str
                    this string represents a node consisting of the identifier followed by the value separated by space
                graph : Graph
                    this is the fundamental graph to be parsed from the TGF-file
        """
        f = open("/Users/MyUsername/PycharmProjects/firstGraphProject/data/tgf_graph_structure.txt", 'r')
        delimiter_reached = False

        lines = f.readlines()
        for line in lines:
            if line == "#\n":
                delimiter_reached = True
            if delimiter_reached:
                print("delimeter reached")
                # readEdges(line)
            else:
                Parser.read_nodes(line, graph)
