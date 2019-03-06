class Node:
    """
            A class used to represent a Node

            Attributes
            ----------
            identifier : int
               A unique identifier of the node
            value : String
               The value the node is holding
            inc_edges : list
                this list holds all the incoming edges to the node
            out_edges : list
                this list holds all the outgoing edges from the node

            Methods
            -------
            __str__()
                Override the __str()__ for proper textual representation of a node
    """

    def __init__(self, identifier, value, inc_edges=None, out_edges=None):
        """
                Parameters
                ----------
                identifier : int
                   A unique identifier of the node
                value : String
                   The value the node is holding
                inc_edges : list
                   This list holds all the incoming edges to the node
                out_edges : list
                   This list holds all the outgoing edges from the node
        """
        self.identifier = identifier
        self.value = value
        self.inc_edges = inc_edges if inc_edges is not None else list()
        self.out_edges = out_edges if out_edges is not None else list()

    def __str__(self):
        """
                Override the __str()__ for a proper textual representation of a node
                Parameters
                ----------
        """
        print('This is node {} and my value is {}'.format(self.identifier, self.value))
        print('My incoming edges are:')
        for edge in self.inc_edges:
            edge.__str__()
        print('My outgoing edges are:')
        for edge in self.out_edges:
            edge.__str__()
