from firstGraphProject.model.graph import Graph
from firstGraphProject.model.node import Node


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
    def parse_tgf_file(graph: Graph, path):
        """
        This method parses the whole file to create nodes and connect them.
        The common format for the nodes can be found at the read_nodes() docstring.

        Nodes and Edges are separated by a #. When # is reached, the (but possibly there will be no connections at all)
        the read_edges() will be invoked.
        Edge Format: [identifier of source_node] [identifier of target_node]

                Parameters
                ----------
                path:
                    the path (as a command line parameter) specifies the files location
                graph : Graph
                    this is the fundamental graph to be parsed from the TGF-file
        """
        f = open(path, 'r')
        delimiter_reached = False

        lines = f.readlines()
        for line in lines:
            if line == "#\n":
                delimiter_reached = True
                continue
            if delimiter_reached:
                Parser.read_edges(line, graph)
            else:
                Parser.read_nodes(line, graph)

    @staticmethod
    def read_edges(edge_line, graph: Graph):
        """
            This method parses the TGF representation of an edge.
            Note: The common format for the nodes can be found at the read_nodes() docstring.

            After reaching the delimiter ("#"), this method will parse the TGF representation of an edge and connect
            the corresponding nodes.
            Edge Format: [identifier of source_node] [identifier of target_node]

                    Parameters
                    ----------
                    edge_line:str
                        the
                    graph : Graph
                        this is the fundamental graph to be parsed from the TGF-file
            """
        edge_line_splitted = edge_line.split()
        source_node = None
        target_node = None
        for node in graph.allNodes:
            if node.identifier == edge_line_splitted[0]:
                source_node = node
            elif node.identifier == edge_line_splitted[1]:
                target_node = node
        if source_node is not None and target_node is not None:
            graph.connect(source_node, target_node)
