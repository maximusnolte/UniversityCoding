"""Unit tests for the node_visualizer module."""

__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

import unittest
from node_visualizer import get_node_color

class TestNodeVisualizer(unittest.TestCase):

    def test_get_node_color(self):
        nodes = {
            "A": ("B", "C"),
            "B": ("C",),
            "C": ()
        }

        self.assertEqual(get_node_color("A", nodes), "green")
        self.assertEqual(get_node_color("B", nodes), "blue")
        self.assertEqual(get_node_color("C", nodes), "red")

if __name__ == '__main__':
    unittest.main()