from node import Node


class Edge:
    """
        A class used to represent an Edge

        Attributes
        ----------
        source : list
           the edges´ source node
        destination : list
            the edges´ destination node

        Methods
        -------
        __str__()
            Override the __str()__ for proper textual representation of an edge
        """

    def __init__(self, source: Node, destination: Node):
        """
                Parameters
                ----------
                source : str
                    the edges´ source node
                destination : str
                    the edges´ destination node
        """
        self.source = source
        self.destination = destination
        self.label = "connecting node {} with node {}".format(source.identifier, destination.identifier)

    def __str__(self):
        """
                Override the __str()__ for proper textual representation of an edge

                Parameters
                ----------
        """
        print(self.label)
