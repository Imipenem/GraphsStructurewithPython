from firstGraphProject.model.edge import Edge
from firstGraphProject.model.node import Node


class Graph:
    """
            A class used to represent a Graph

            Attributes
            ----------
            allEdges : list
                this list contains all edges of this graph
            allNodes : list
                this list contains all nodes of this graph

            Methods
            -------
            add_node(*nodes=Node)
                this method adds several nodes to the graph
    """

    def __init__(self, all_edges=None, all_nodes=None):
        """
                Parameters
                ----------
                all_edges : str
                    this list contains all edges of this graph
                all_nodes : str
                    this list contains all nodes of this graph
        """
        self.allEdges = all_edges if all_edges is not None else list()
        self.allNodes = all_nodes if all_nodes is not None else list()

    def add_node(self, *nodes):
        """
        This method adds several nodes to the graph without connecting them.

        However, if the node is already in the graph, it won´t be added twice.

                Parameters
                ----------
                *nodes : Node
                     this list contains all nodes that need to be added to the graph
        """
        for node in nodes:
            if self.allNodes.__contains__(node):
                raise ValueError('Already added node {} to the graph'.format(node.identifier))
            else:
                self.allNodes.append(node)

    def connect(self, source_node: Node, dest_node: Node):
        """
        This method connects to nodes together by creating a new edge.

        Note that the nodes won´t be connected if there´s already a connection or both nodes are the same node.

        However, if the node is already in the graph, it won´t be added twice.

                    Parameters
                    ----------
                    source_node : Node
                        this will be the source node for the new connection
                    dest_node : Node
                        this will be the target node for the new connection
        """
        if source_node is dest_node:
            raise ValueError("Node {} and Node {} are the same nodes; they cannot be connected".format(
                source_node.identifier, dest_node.identifier))
        elif self.has_connection(source_node, dest_node):
            raise ValueError("Node {} and Node {} are already connected".format(source_node.identifier,
                                                                                dest_node.identifier))
        else:
            new_edge = Edge(source_node, dest_node)
            source_node.out_edges.append(new_edge)
            dest_node.inc_edges.append(new_edge)
            self.allEdges.append(new_edge)

    def has_connection(self, source: Node, target: Node):
        """
                This method checks whether to nodes are connected or not by checking both directions.

                            Parameters
                            ----------
                            source : Node
                                the questionable source node (or target node)
                            target : Node
                                the questionable target node (or source node)
        """
        for edge in self.allEdges:
            if (edge.source is source or edge.destination is source) and (edge.destination is target or edge.source
                                                                          is target):
                return True
        return False

    def disconnect(self, source: Node, target: Node):
        """
                This method disconnect two nodes after checking, if they have a connection.
                It will also remove the edge from both nodes´ edge-lists.

                            Parameters
                            ----------
                            source : Node
                                the source node to be disconnected from the target node
                            target : Node
                                the target node to be disconnected from the source node
        """
        if not self.has_connection(source, target):
            raise ValueError("Error while disconnecting: Node {} and Node {} are not connected".format(
                source.identifier, target.identifier))
        else:
            for edge in self.allEdges:
                if edge.source is source and edge.destination is target or edge.source is target and edge.destination \
                        is source:
                    self.allEdges.remove(edge)
                    source.out_edges.remove(edge) if source is edge.source else source.inc_edges.remove(edge)
                    target.inc_edges.remove(edge) if target is edge.destination else target.out_edges.remove(edge)
                    break
