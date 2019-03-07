from firstGraphProject.model.graph import Graph


class Writer:
    """
            This class represents a writer to parse an actual existing graph into it´s TGF-format

            Attributes
            ----------

            Methods
            -------
            write_to_tgf
                this method parses the graph into a file at the location
    """

    @staticmethod
    def write_to_tgf(graph: Graph, path):
        """
                This method parses the graph to a TGF-file (for TGF-format see class Parser documentation)


                        Parameters
                        ----------
                        graph : Graph
                             the actual existing graph

                        path : str
                             the path , the writer pareses the file to given as a command line parameter
        """

        with open(path, 'w') as f:
            for node in graph.allNodes:
                # f.write(node.identifier + " " + node.value + "\n")
                f.write("{} {}\n".format(node.identifier, node.value))
            f.write('#' + "\n")

            for edge in graph.allEdges:
                # f.write(edge.source.identifier + " " + edge.destination.identifier + "\n")
                f.write("{} {}\n".format(edge.source.identifier, edge.destination.identifier))
