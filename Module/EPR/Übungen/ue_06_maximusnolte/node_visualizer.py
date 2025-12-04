from math import degrees, atan2
import turtle as t

def calculate_outgoing_degree(node_in, nodes_in):
    """Calculates the outgoing degree of a node.
    """
    connections = nodes_in[node_in]
    return len(connections) + 1


def calculate_incoming_degree(node_in, nodes_in):
    """Calculates the incoming degree of a node."""
    count = 0
    for k in nodes_in:
        connections = nodes_in[k]
        if node_in in connections:
            count += 1
    return count


def calculate_angle(start_position, end_position):
    """Calculates the angle between two positions."""
    angle = degrees(atan2(end_position[1] - start_position[1],
                                    end_position[0] - start_position[0]))
    return angle


def draw_node(node, position, color, size, offset=(0, 0)):
    """Draws a single node at a given position."""
    print(f"Drawing Knot: ({node}) at position: {position[0] + offset[0]}, "
          f"{position[1] + offset[1]} with color: {color}")
    t.teleport(position[0] + offset[0], position[1] + offset[1])
    t.dot(size, color)
    t.write(node)


def draw_connection(start_position, end_position, directional=False,
                    offset=(0, 0)):
    """Draws a connection between two nodes."""
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
    """Determines the color of a node based on its degrees."""
    outgoing_degree = calculate_outgoing_degree(node_in, nodes_in)
    incoming_degree = calculate_incoming_degree(node_in, nodes_in)
    if outgoing_degree == 1:
        return "red"
    if incoming_degree == 0:
        return "green"
    return "blue"


# Draw connections
def finish_drawing():
    """Finalizes the drawing."""
    t.hideturtle()
    t.done()


def draw_nodes(nodes_in, nodes_positions_in, size=10, offset=(0, 0)):
    """Draws a dict of nodes at given positions."""
    t.tracer(0)
    for node in nodes_in:
        position = nodes_positions_in[node]
        color = get_node_color(node, nodes_in)
        draw_node(node, position, color, size, offset)
    t.update()


def draw_connections(nodes_in, nodes_positions_in, directional=False,
                     offset=(0, 0)):
    """Draws connections between nodes."""
    t.tracer(1)
    for node in nodes_in:
        start_position = nodes_positions_in[node]
        connections = nodes_in[node]
        for connected_node in connections:
            end_position = nodes_positions_in[connected_node]
            draw_connection(start_position, end_position, directional, offset)


def draw_legend(position=(200, 200), offset=20):
    """Draws a legend for the node colors."""
    t.tracer(0)
    t.teleport(position[0], position[1])
    t.write("Legend:")
    t.teleport(position[0], position[1] - offset)
    t.dot(10, "red")
    t.write(" Knoten mit Ausgangsgrad 1")
    t.teleport(position[0], position[1] - (2 * offset))
    t.dot(10, "green")
    t.write(" Knoten mit Eingangsgrad 0")
    t.teleport(position[0], position[1] - (3 * offset))
    t.dot(10, "blue")
    t.write(" Knoten mit sonstigen Graden")
    t.update()


def calculate_edge_count(nodes_in, directed=False):
    """Calculates the number of edges in the graph."""
    if directed:
        edge_count = 0
        for node in nodes_in:
            connections = nodes_in[node]
            edge_count += len(connections)
        return edge_count

    edge_count = 0
    for neighbors in nodes_in.values():
        edge_count += len(neighbors)
    return edge_count // 2


def check_edge_count(nodes_in, directed=False):
    """Checks if the edge count matches the expected value for a tree."""
    edge_count = calculate_edge_count(nodes_in, directed)
    if edge_count == len(nodes_in) - 1:
        return True
    return False

def node_visualizer(window_size=(1000,1000), speed=0):
    t.setup(window_size[0], window_size[1])
    t.speed(speed)
