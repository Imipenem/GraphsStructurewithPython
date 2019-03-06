from firstGraphProject.model.node import Node
from dataclasses import dataclass, field


@dataclass()
class Edge:
    """
        A class used to represent an Edge

        Attributes
        ----------
        source : Node
           the edges´ source node
        destination : Node
            the edges´ destination node

        Methods
        -------
        __str__()
            Override the __str()__ for proper textual representation of an edge
        """

    source: Node = field(default_factory=Node)
    destination: Node = field(default_factory=Node)
    label: str = ""

    def __str__(self):
        """
                Override the __str()__ for proper textual representation of an edge

                Parameters
                ----------
        """
        label = "connecting node {} with node {}".format(self.source.identifier, self.destination.identifier)
        return label
