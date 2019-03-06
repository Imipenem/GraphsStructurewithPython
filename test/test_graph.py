#!/usr/bin/env python

import unittest
from firstGraphProject.model.graph import Graph
from firstGraphProject.model.edge import Edge
from firstGraphProject.model.node import Node


class TestGraph(unittest.TestCase):

    def test_add_node_with_one_node(self):
        """ Check if one node is added to the graph

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_graph = Graph()
        test_graph.add_node(test_node_1)
        self.assertEqual(test_node_1, test_graph.allNodes[0])

    def test_add_node_with_more_nodes(self):
        """ Check if more nodes are added to the graph

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')
        test_node_5 = Node(5, 'Node5')
        test_node_6 = Node(6, 'Node6')
        test_graph = Graph()
        test_graph.add_node(test_node_1, test_node_2, test_node_3, test_node_4, test_node_5, test_node_6)
        test_node_list = [test_node_1, test_node_2, test_node_3, test_node_4, test_node_5, test_node_6]

        self.assertEqual(test_node_list, test_graph.allNodes)

    def test_add_node_with_node_that_is_already_added(self):
        """ Check if it raises a ValueError if one node is added twice

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_graph = Graph()
        test_graph.add_node(test_node_1)
        with self.assertRaises(ValueError):
            test_graph.add_node(test_node_1)

    def test_add_node_with_more_nodes_that_are_already_added(self):
        """ Check if it raises a ValueError if multiple nodes are added twice

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')
        test_node_5 = Node(5, 'Node5')
        test_node_6 = Node(6, 'Node6')
        test_graph = Graph()
        test_graph.add_node(test_node_1, test_node_2, test_node_3, test_node_4, test_node_5, test_node_6)
        with self.assertRaises(ValueError):
            test_graph.add_node(test_node_6, test_node_5, test_node_3)

    def test_connect_with_two_nodes(self):
        """ Check if it connects two nodes with an edge an add it to the graph

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_edge = Edge(test_node_1, test_node_2)
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        self.assertEqual(test_graph.allEdges[0], test_edge)

    def test_connect_more_nodes(self):
        """ Check if it connects multiple nodes with an edge an add it to the graph

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')
        test_node_5 = Node(5, 'Node5')
        test_node_6 = Node(6, 'Node6')
        test_edge1 = Edge(test_node_1, test_node_2)
        test_edge2 = Edge(test_node_2, test_node_3)
        test_edge3 = Edge(test_node_3, test_node_4)
        test_edge4 = Edge(test_node_4, test_node_5)
        test_edge5 = Edge(test_node_5, test_node_6)
        test_edge6 = Edge(test_node_6, test_node_1)
        test_edges_list = [test_edge1, test_edge2, test_edge3, test_edge4, test_edge5, test_edge6]
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        test_graph.connect(test_node_2, test_node_3)
        test_graph.connect(test_node_3, test_node_4)
        test_graph.connect(test_node_4, test_node_5)
        test_graph.connect(test_node_5, test_node_6)
        test_graph.connect(test_node_6, test_node_1)

        self.assertEqual(test_edges_list, test_graph.allEdges)

    def test_connect_two_nodes_that_are_already_connected(self):
        """ Check if the it raises a ValueError if two nodes that are already connected should be connected again

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        with self.assertRaises(ValueError):
            test_graph.connect(test_node_1, test_node_2)

    def test_connect_loop_node_not_allowed(self):
        """ Check if raises a ValueError while tying to establish a self-loop

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_graph = Graph()
        with self.assertRaises(ValueError):
            test_graph.connect(test_node_1, test_node_1)

    def test_connect_two_nodes_that_are_already_connected_with_source_and_destination_changed(self):
        """ Check if it raises a ValueError if source and target node are changed (but connected nevertheless)

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        with self.assertRaises(ValueError):
            test_graph.connect(test_node_2, test_node_1)

    def test_has_connection_false(self):
        """ Check if hasConnection() returns false for nodes that aren´t connected

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        self.assertFalse(test_graph.has_connection(test_node_1, test_node_2))

    def test_has_connection_true(self):
        """ Check if hasConnection() returns true for nodes that are connected

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        self.assertTrue(test_graph.has_connection(test_node_1, test_node_2))

    def test_has_connection_true_nodes_changed(self):
        """ Check if hasConnection() returns true for nodes that are connected (the other way)

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        self.assertTrue(test_graph.has_connection(test_node_2, test_node_1))

    def test_disconnect_two_nodes(self):
        """ Check if it disconnects two nodes and removes the edge from the graphs edges

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        test_graph.disconnect(test_node_1, test_node_2)
        test_edge_list = []

        self.assertEqual(test_edge_list, test_graph.allEdges)

    def test_disconnect_more_nodes(self):
        """ Check if it disconnects multiple nodes and removes the edges from the graphs edges

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')
        test_node_5 = Node(5, 'Node5')
        test_node_6 = Node(6, 'Node6')

        test_edge2 = Edge(test_node_2, test_node_3)
        test_edge5 = Edge(test_node_5, test_node_6)
        test_edge6 = Edge(test_node_6, test_node_1)

        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        test_graph.connect(test_node_2, test_node_3)
        test_graph.connect(test_node_3, test_node_4)
        test_graph.connect(test_node_4, test_node_5)
        test_graph.connect(test_node_5, test_node_6)
        test_graph.connect(test_node_6, test_node_1)

        test_graph.disconnect(test_node_1, test_node_2)
        test_graph.disconnect(test_node_3, test_node_4)
        test_graph.disconnect(test_node_4, test_node_5)
        test_edges_list_after_disconnect = [test_edge2, test_edge5, test_edge6]

        self.assertEqual(test_edges_list_after_disconnect, test_graph.allEdges)

    def test_disconnect_with_nodes_that_are_not_connected(self):
        """ Check if it raises a ValueError when trying to disconnect two nodes that are not connected

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_graph = Graph()

        with self.assertRaises(ValueError):
            test_graph.disconnect(test_node_1, test_node_2)

    def test_disconnect_with_nodes_that_are_connected_the_other_way(self):
        """ Check if it disconnects two nodes that are connected (but the other way) and removes the edge from the
            graphs list

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(5, 'Node5')
        test_node_4 = Node(6, 'Node6')

        test_edge1 = Edge(test_node_1, test_node_2)
        test_edge3 = Edge(test_node_3, test_node_4)
        test_edge4 = Edge(test_node_4, test_node_1)

        test_graph = Graph()
        test_graph.connect(test_node_1, test_node_2)
        test_graph.connect(test_node_2, test_node_3)
        test_graph.connect(test_node_3, test_node_4)
        test_graph.connect(test_node_4, test_node_1)

        test_graph.disconnect(test_node_3, test_node_2)

        test_edges_list_after_disconnect = [test_edge1, test_edge3, test_edge4]

        self.assertEqual(test_edges_list_after_disconnect, test_graph.allEdges)


