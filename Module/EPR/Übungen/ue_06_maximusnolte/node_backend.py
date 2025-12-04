
from math import ceil, sqrt, degrees, atan2

def append_node(node_in, nodes_in):
    """Appends a new node to the nodes dictionary.
        :param node_in: Node to append.
        :param nodes_in: dict - The existing nodes dictionary.
        :return: dict - A dictionary of nodes with the new node added.
    """
    node_in = str(node_in)
    if node_in not in nodes_in:
        node_in = {node_in: ()}
        nodes_in.update(node_in)
        return nodes_in
    return None


def set_node_connections(node_in, nodes_in, new_connections):
    """Sets new connections for a given node.
        :param node_in: Node to set connections for.
        :param nodes_in: dict - The existing nodes dictionary.
        :param new_connections: tuple - The new connections to set.
        :return: dict - A dictionary of nodes with updated connections.

    """
    if node_in in nodes_in:
        nodes_in[node_in] = new_connections
        return nodes_in
    return None


def generate_node_positions(nodes_in, distance=100):
    """Generates positions for nodes in a grid layout.
        :param nodes_in: dict - The existing nodes dictionary.
        :param distance: int - The distance between nodes.
        :return: dict - A dictionary of nodes with their positions.
    """
    print("Generating positions for nodes...")
    cols = ceil(sqrt(len(nodes_in)))

    positions = {}
    for i, node in enumerate(nodes_in):
        row = i // cols
        col = i % cols
        positions.update({node : (col * distance, row * distance)})
    print(f"Finished generating positions for nodes. Positions: {positions}")
    return positions


def convert_string_connections(input_string, nodes, directional):
    print("Converting string to connections...")

    input_string = input_string.strip()
    if ";" not in input_string:
        print("Invalid input format. Please separate entries with semicolons.")
        return None

    entries = input_string.split(';')

    for entry in entries:
        entry = entry.strip()
        if entry == "":
            continue

        if ":" not in entry or entry.count(":") != 1:
            print(f"Invalid entry: {entry}")
            return None

        node, raw_connections = entry.split(":")
        node = node.strip()
        raw_connections = raw_connections.strip()

        connected_nodes = []
        for c in raw_connections.split(","):
            c = c.strip()
            if c != "":
                connected_nodes.append(c)

        connected_nodes = tuple(connected_nodes)

        # Node existiert nicht
        if node not in nodes:
            print(f"Knot {node} does not exist.")
            return None

        # Setze die direkten Verbindungen
        nodes[node] = connected_nodes

        # Falls directional=True: Rückverbindungen setzen
        if not directional:
            for cnode in connected_nodes:
                if cnode not in nodes:
                    print(f"Knot {cnode} does not exist.")
                    return None

                # alte connections holen
                existing = list(nodes[cnode])

                # rückverbindung hinzufügen falls nicht existiert
                if node not in existing:
                    existing.append(node)

                nodes[cnode] = tuple(existing)

    print("Converted connections:")
    print(nodes)
    return nodes



def generate_node_dict(number_of_nodes):
    """Generates a dictionary of nodes with no connections.
        :param number_of_nodes: Number of nodes.
        :return: dict - A dictionary of nodes with no connections.
    """
    nodes = {}
    for i in range(number_of_nodes):
        append_node(i+1, nodes)
    return nodes


def calculate_outgoing_degree(node_in, nodes_in):
    """Calculates the outgoing degree of a node.
        :param node_in: str - The node to calculate the outgoing degree for.
        :param nodes_in: dict - The existing nodes dictionary.
        :return: int - The outgoing degree of the node.
    """
    connections = nodes_in[node_in]
    return len(connections)


def calculate_incoming_degree(node_in, nodes_in):
    """Calculates the incoming degree of a node.
        :param node_in: str - The node to calculate the incoming degree for.
        :param nodes_in: dict - The existing nodes dictionary.
        :return: int - The incoming degree of the node.
    """
    count = 0
    for k in nodes_in:
        connections = nodes_in[k]
        if node_in in connections:
            count += 1
    return count


def calculate_angle(start_position, end_position):
    """Calculates the angle between two positions.
        Calculating the angle in degrees using atan2 because it can
        calculate the angle based on the difference in y and x coordinates
        directly. Converting radians to degrees for Turtle compatibility.
        :param start_position: int - The start position of the angle.
        :param end_position: int - The end position of the angle.
        :return: int - The angle between the two positions.
    """
    angle = degrees(atan2(end_position[1] - start_position[1],
                                    end_position[0] - start_position[0]))
    return angle