"""Unit tests for node_backend module."""

__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

import unittest

from node_backend import *


class TestNodeBackend(unittest.TestCase):

    def test_append_node(self):
        nodes = {}
        nodes = append_node("A", nodes)
        self.assertIn("A", nodes)
        self.assertEqual(nodes["A"], ())

        append_node("B", nodes)
        self.assertIn("B", nodes)
        self.assertEqual(nodes["B"], ())

        append_node("A", nodes)
        self.assertEqual(len(nodes), 2)

    def test_set_node_connections(self):
        nodes = {"A": (), "B": ()}
        nodes = set_node_connections("A", nodes, ("B",))
        self.assertEqual(nodes["A"], ("B",))

        nodes = set_node_connections("B", nodes, ("A",))
        self.assertEqual(nodes["B"], ("A",))
        self.assertIsNone(set_node_connections("C", nodes, ("B",)))

    def test_generate_node_positions(self):
        nodes = {"A": (), "B": (), "C": (), "D": ()}
        positions = generate_node_positions(nodes, distance=100)
        expected_positions = {
            "A": (0, 0),
            "B": (100, 0),
            "C": (0, 100),
            "D": (100, 100)
        }
        self.assertEqual(positions, expected_positions)
        positions = generate_node_positions(None, distance=100)
        self.assertEqual(positions, None)

    def test_convert_string_connections(self):
        nodes = {"A": (), "B": (), "C": ()}

        self.assertEqual(convert_string_connections("", nodes,
                                                    True),
                                                    None)
        self.assertEqual(convert_string_connections("A:B;B:C;C:;",
                                                     nodes,
                                                     True),
                                                     {
                                                            "A": ("B",),
                                                            "B": ("C",),
                                                            "C": ()
                                                        })
        self.assertEqual(convert_string_connections("A:B;B:C;",
                                                     nodes,
                                                     False),
                                                     {
                                                            "A": ("B",),
                                                            "B": ("C", "A"),
                                                            "C": ("B",)
                                                        })

    def test_generate_node_dict(self):
        expected_nodes = {'1': (),'2': (),'3': (),'4': ()}
        self.assertEqual(generate_node_dict(4),expected_nodes)
        expected_nodes = {}
        self.assertEqual(generate_node_dict(0),expected_nodes)
        expected_nodes = {'1': (), '2': (), '3': (), '4': (), '5': ()}
        self.assertEqual(generate_node_dict(5),expected_nodes)

    def test_calculate_outgoing_degree(self):

        nodes = {
            "A": ("B", "C"),
            "B": ("C",),
            "C": ()
        }
        self.assertEqual(calculate_outgoing_degree("A", nodes), 2)
        self.assertEqual(calculate_outgoing_degree("B", nodes), 1)
        self.assertEqual(calculate_outgoing_degree("C", nodes), 0)

    def test_calculate_incoming_degree(self):

        nodes = {
            "A": ("B", "C"),
            "B": ("C",),
            "C": ()
        }
        self.assertEqual(calculate_incoming_degree("A", nodes), 0)
        self.assertEqual(calculate_incoming_degree("B", nodes), 1)
        self.assertEqual(calculate_incoming_degree("C", nodes), 2)

    def test_calculate_angle(self):
        position = (0,0)
        position2 = (1,0)
        self.assertEqual(calculate_angle(position, position2), 0)
        position2 = (0,1)
        self.assertEqual(calculate_angle(position, position2), 90)
        position2 = (-1,0)
        self.assertEqual(calculate_angle(position, position2), 180)


if __name__ == '__main__':
    unittest.main()
