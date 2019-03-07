from dataclasses import dataclass, field


@dataclass()
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

    identifier: int
    value: str
    inc_edges: list = field(default_factory=list)
    out_edges: list = field(default_factory=list)

    def __str__(self):
        """
                Override the __str()__ for a proper textual representation of a node
                Parameters
                ----------
        """
        print('This is node {} and my value is {}'.format(self.identifier, self.value))
        print('My incoming edges are:')
        for edge in self.inc_edges:
            print(edge.__str__())
        print('My outgoing edges are:')
        for edge in self.out_edges:
            print(edge.__str__())
