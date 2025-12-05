"""Module for visualizing nodes and their connections using Turtle graphics."""

__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

from node_backend import (calculate_incoming_degree,
                          calculate_outgoing_degree,
                          calculate_angle)
import turtle as t


def draw_node(node, position, color, size, offset=(0, 0)):
    """Draws a single node with a color, size and offset
        at a given position using Turtle.
        :param node: Node to draw.
        :param position: Position to draw the node at.
        :param color: Color of the node.
        :param size: Size of the node.
        :param offset: Offset to apply to the position.
    """
    print(f"Drawing Knot: ({node}) at position: {position[0] + offset[0]}, "
          f"{position[1] + offset[1]} with color: {color}")
    t.teleport(position[0] + offset[0], position[1] + offset[1])
    t.dot(size, color)
    t.write(node, font=("Arial", 16, "normal"))


def draw_connection(start_position, end_position, directional=False,
                    offset=(0, 0)):
    """Draws a connection between two nodes using Turtle.
        :param start_position: Start position of the connection.
        :param end_position: End position of the connection.
        :param directional: Whether the connection is directional.
        :param offset: Offset to apply to the positions.
    """
    angle = calculate_angle(start_position, end_position)
    print(f"Drawing Connection from: {start_position} to: {end_position}")
    t.teleport(start_position[0] + offset[0],
               start_position[1] + offset[1])
    t.setheading(angle)
    t.pendown()
    t.goto(end_position[0] + offset[0], end_position[1] + offset[1])
    if directional:
        t.stamp()
    t.penup()


def get_node_color(node_in, nodes_in):
    """Determines the color of a node based on its degrees.
        :param node_in: str - The node to determine the color for.
        :param nodes_in: dict - The existing nodes dictionary.
        :return: str - The color of the node.
    """
    outgoing_degree = calculate_outgoing_degree(node_in, nodes_in)
    incoming_degree = calculate_incoming_degree(node_in, nodes_in)
    if outgoing_degree == 0 and not incoming_degree == 0:
        return "red"
    if incoming_degree == 0 and not outgoing_degree == 0:
        return "green"
    if incoming_degree == 0 and outgoing_degree == 0:
        return "black"
    return "blue"


# Draw connections
def finish_drawing():
    """Finalizes the drawing."""
    t.hideturtle()
    t.done()


def draw_nodes(nodes_in, nodes_positions_in, size=10, offset=(0, 0)):
    """Draws a dict of nodes at given positions.
        :param nodes_in: dict - The existing nodes dictionary.
        :param nodes_positions_in: dict - The positions of the nodes.
        :param size: Size of the nodes.
        :param offset: Offset to apply to the positions.
    """
    t.tracer(0)
    for node in nodes_in:
        position = nodes_positions_in[node]
        color = get_node_color(node, nodes_in)
        draw_node(node, position, color, size, offset)
    t.update()


def draw_connections(nodes_in, nodes_positions_in, directional=False,
                     offset=(0, 0)):
    """Draws connections between nodes.
        :param nodes_in: dict - The existing nodes dictionary.
        :param nodes_positions_in: dict - The positions of the nodes.
        :param directional: Whether the connections are directional.
        :param offset: Offset to apply to the positions.
    """
    t.tracer(1)
    for node in nodes_in:
        start_position = nodes_positions_in[node]
        connections = nodes_in[node]
        for connected_node in connections:
            end_position = nodes_positions_in[connected_node]
            draw_connection(start_position, end_position, directional, offset)


def draw_legend(position=(250, -400), offset=20):
    """Draws a legend for the node colors.
        :param position: Position to draw the legend at. (default: (200, 200))
        :param offset: Offset between legend entries. (default: 20)
    """
    print(f"Drawing Legend at: {position[0]} to {position[1]}")
    t.tracer(0)
    t.teleport(position[0], position[1])
    t.write("Legende:", font=("Arial", 16, "normal"))
    t.teleport(position[0], position[1] - offset)
    t.dot(10, "red")
    t.write(" End-Knoten mit Ausgangsgrad 0", font=("Arial", 16,
            "normal"))
    t.teleport(position[0], position[1] - (2 * offset))
    t.dot(10, "green")
    t.write(" Start-Knoten mit Eingangsgrad 0", font=("Arial", 16,
            "normal"))
    t.teleport(position[0], position[1] - (3 * offset))
    t.dot(10, "blue")
    t.write(" Knoten mit sonstigen Graden", font=("Arial", 16,
            "normal"))
    t.teleport(position[0], position[1] - (4 * offset))
    t.dot(10, "black")
    t.write(" Isolierter Knoten", font=("Arial", 16, "normal"))
    t.hideturtle()
    t.update()


def node_visualizer(window_size=(1000, 1000), speed=0):
    """Sets up the turtle graphics window.
        :param window_size: Tuple - The size of the window.
        (default: (1000, 1000))
        :param speed: int - The speed of the turtle. (default: 0)
    """
    t.setup(window_size[0], window_size[1])
    t.speed(speed)
