#!/usr/bin/env python

import unittest
import os

from test_util.path_util import pf

from firstGraphProject.model.graph import Graph
from firstGraphProject.model.node import Node
from firstGraphProject.parse_write.parser import Parser
from firstGraphProject.parse_write.writer import Writer

WD = os.path.dirname(__file__)
PATH_TO_TGF_TESTFILE_1 = pf(WD, "data/test_tgf_parser1.txt")
PATH_TO_TGF_TESTFILE_2 = pf(WD, "data/test_tgf_parser_2.txt")
PATH_TO_TEST_READ_NODES = pf(WD, "data/test_read_nodes")
PATH_TO_TEST_READ_EDGES = pf(WD, "data/test_read_edges")


class TestParserAndWriter(unittest.TestCase):

    def test_parse_tgf_to_graph(self):
        """ Check if the parser correctly parses a graph from a TGF-File

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')

        test_graph = Graph()
        control_graph = Graph()
        control_graph.add_node(test_node_1)
        control_graph.add_node(test_node_2)
        control_graph.connect(test_node_1, test_node_2)

        Parser.parse_tgf_file(test_graph, PATH_TO_TGF_TESTFILE_1)
        self.assertEqual(test_graph.allNodes, control_graph.allNodes)
        self.assertEqual(test_graph.allEdges, control_graph.allEdges)

    def test_parse_tgf_to_graph_2(self):
        """ Check if the parser correctly parses a graph from a TGF-File

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')

        test_graph = Graph()
        control_graph = Graph()
        control_graph.add_node(test_node_1)
        control_graph.add_node(test_node_2)
        control_graph.add_node(test_node_3)
        control_graph.add_node(test_node_4)
        control_graph.connect(test_node_1, test_node_2)
        control_graph.connect(test_node_2, test_node_3)
        control_graph.connect(test_node_3, test_node_4)
        control_graph.connect(test_node_4, test_node_1)

        Parser.parse_tgf_file(test_graph, PATH_TO_TGF_TESTFILE_2)
        self.assertEqual(test_graph.allNodes, control_graph.allNodes)
        self.assertEqual(test_graph.allEdges, control_graph.allEdges)

    def test_read_nodes(self):
        """ Check if the parser parses nodes correctly

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')
        test_node_5 = Node(5, 'Node5')
        test_node_6 = Node(6, 'Node6')
        test_node_7 = Node(7, 'Node7')
        test_node_8 = Node(8, 'Node8')
        test_node_9 = Node(9, 'Node9')
        test_node_10 = Node(10, 'Node10')
        test_node_11 = Node(11, 'Node11')
        test_node_12 = Node(12, 'Node12')
        test_node_13 = Node(13, 'Node13')
        test_node_14 = Node(14, 'Node14')
        test_node_15 = Node(15, 'Node15')
        test_node_16 = Node(16, 'Node16')

        control_graph = Graph()
        control_graph.add_node(test_node_1)
        control_graph.add_node(test_node_2)
        control_graph.add_node(test_node_3)
        control_graph.add_node(test_node_4)
        control_graph.add_node(test_node_5)
        control_graph.add_node(test_node_6)
        control_graph.add_node(test_node_7)
        control_graph.add_node(test_node_8)
        control_graph.add_node(test_node_9)
        control_graph.add_node(test_node_10)
        control_graph.add_node(test_node_11)
        control_graph.add_node(test_node_12)
        control_graph.add_node(test_node_13)
        control_graph.add_node(test_node_14)
        control_graph.add_node(test_node_15)
        control_graph.add_node(test_node_16)

        test_graph = Graph()

        Parser.parse_tgf_file(test_graph, PATH_TO_TEST_READ_NODES)
        self.assertEqual(test_graph.allNodes, control_graph.allNodes)

    def test_read_edges(self):
        """ Check if the parser parses edges correctly

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        test_node_1 = Node(1, 'Node1')
        test_node_2 = Node(2, 'Node2')
        test_node_3 = Node(3, 'Node3')
        test_node_4 = Node(4, 'Node4')

        test_graph = Graph()
        control_graph = Graph()
        control_graph.add_node(test_node_1)
        control_graph.add_node(test_node_2)
        control_graph.add_node(test_node_3)
        control_graph.add_node(test_node_4)
        control_graph.connect(test_node_1, test_node_2)
        control_graph.connect(test_node_2, test_node_4)
        control_graph.connect(test_node_1, test_node_3)

        Parser.parse_tgf_file(test_graph, PATH_TO_TEST_READ_EDGES)
        self.assertEqual(test_graph.allEdges, control_graph.allEdges)
