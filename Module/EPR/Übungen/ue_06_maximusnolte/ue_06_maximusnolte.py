
from math import ceil, sqrt
from node_visualizer import *
from copy import deepcopy



def append_node(node_in, nodes_in):
    """Appends a new node to the nodes dictionary."""
    node_in = str(node_in)
    if node_in not in nodes_in:
        node_in = {node_in: ()}
        nodes_in.update(node_in)
        return nodes_in
    return None


def set_node_connections(node_in, nodes_in, new_connections):
    """Sets new connections for a given node."""
    if node_in in nodes_in:
        nodes_in[node_in] = new_connections
        return nodes_in
    return None


def generate_node_positions(nodes_in, distance=100):
    """Generates positions for nodes in a grid layout."""
    print("Generating positions for nodes...")
    cols = ceil(sqrt(len(nodes_in)))

    positions = {}
    for i, node in enumerate(nodes_in):
        row = i // cols
        col = i % cols
        positions.update({node : (col * distance, row * distance)})
    print(f"Finished generating positions for nodes. Positions: {positions}")
    return positions


def convert_string_connections(input_string, nodes):
    """Converts a string representation of connections into a dict."""
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

        node, connected_nodes_raw = entry.split(":")
        connected_nodes_raw = connected_nodes_raw.strip()

        connected_nodes_raw = connected_nodes_raw.split(",")
        connected_nodes = []
        for connection in connected_nodes_raw:
            if connection != "":
                connected_nodes.append(connection)

        connected_nodes = tuple(connected_nodes)

        if node not in nodes:
            print(f"Knot {node} does not exist.")
            return None

        nodes[node] = connected_nodes

    print("Converted connections:")
    print(nodes)
    return nodes


def generate_node_dict(number_of_nodes):
    """Generates a dictionary of nodes with no connections."""
    nodes = {}
    for i in range(number_of_nodes):
        append_node(i+1, nodes)
    return nodes


def option_handler(option):
    """Handles user options for node input."""
    match option:
        case 1:
            print("How many nodes to generate?")
            number_of_nodes = 0
            while number_of_nodes == 0:
                input_string = input("Number of nodes >")
                try:
                    input_string = int(input_string)
                    if input_string > 0:
                        number_of_nodes = deepcopy(input_string)
                    else:
                        print(
                            "Invalid input. Please enter a positive integer.")
                        number_of_nodes = 0
                except ValueError, TypeError:
                    print("Invalid input. Please enter a positive integer.")
                    number_of_nodes = 0
            return generate_node_dict(number_of_nodes)
        case 2:
            print("Input nodes manually as a valid list like K1;K2;K3;...")
            nodes = None
            while nodes is None:
                input_string = input("Knots >")
                input_string = input_string.strip()
                if ";" in input_string:
                    entries = input_string.split(';')
                    nodes = {}
                    for entry in entries:
                        entry = entry.strip()
                        if entry != "":
                            append_node(entry, nodes)
                else:
                    print(
                        "Invalid input format. Please separate entries with semicolons.")
                    nodes = None
            return nodes
        case 3:
            print("Input node positions manually as a valid dict like: "
                  "x_position, y_position; separated by"
                  "semicolons, Node-Names will be auto-generated")
            nodes = None
            while nodes is None:
                nodes = {}
                input_string = input("Node Positions >")
                if ";" in input_string:
                    entries = input_string.split(';')
                    for i, entry in enumerate(entries):
                        entry = entry.strip().split(",")
                        if entry == ['']:
                            continue
                        else:
                            if len(entry) != 2:
                                print(f"Invalid entry (must have exactly two values): {entry}")
                                nodes = None
                                break
                            x_position = entry[0].strip()
                            y_position = entry[1].strip()
                            if x_position.isdigit() and y_position.isdigit():
                                append_node(i, nodes)
                                set_node_connections(i, nodes, (int(x_position), int(y_position)))
                                print(f"Added node '{i}' with position ({x_position}, {y_position})")
                            else:
                                print(f"Invalid entry ({x_position}, "
                                  f"{y_position}): {entry} got non -integer values")
                                nodes = None
                else:
                    print(
                        "Invalid input format. Please separate entries with semicolons.")
                    nodes = None
            return nodes
    return None


def input_handler():
    """Handles user input for graph configuration."""
    # Setting up directed or undirected graph
    print("----Graph Type----")
    directed = None
    while directed is None:
        input_string = input("Directed graph? (y/n): ").lower()
        if input_string == 'y':
            directed = True
        elif input_string == 'n':
            directed = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            directed = None
    # Setting up nodes
    option = None
    print("----Input Nodes----")
    print("Options:")
    print(
        "1. Automatically Generate Nodes")
    print(
        "2. Input Node Manually (as a valid list like 1;2;3...), seperated "
        "by semicolons")
    print(
        "3. Input Node Positions Manually (as a valid dict like: Knot_Name: "
        "x_position, y_position); separated by semicolons, Knot Names will be auto-generated")
    while option is None:
        input_string = input("Option 1/2/3) >")
        try:
            input_string = int(input_string)
            if input_string in [1, 2, 3]:
                option = deepcopy(input_string)
            else:
                print("Invalid input. Please enter '1', '2', '3'.")
                option = None
        except ValueError, TypeError:
            print("Invalid input. Please enter '1', '2', '3'.")
            option = None
    nodes = option_handler(option)

    # Setting up connections
    connections = None
    print("----Setup Knot-Connections----")
    print("Set Knot Connections (as a valid dict like: "
          "Node_Name: Connected_Node1, Connected_Node2, ...; separated by "
          "semicolons)")
    while connections is None:
        input_string = input("Connections >")
        input_string = input_string.strip()
        connections = convert_string_connections(input_string, nodes)
    nodes = connections

    print("----FinalResult----")
    print(f"Directed: {directed}, Nodes: {nodes}")
    return directed, nodes


if __name__ == '__main__':
    directed_input, nodes_input = input_handler()
    generated_nodes_positions = generate_node_positions(nodes_input, 100)

    node_visualizer(window_size=(1000, 1000), speed=10)
    nodes_offset = (0,0)
    draw_nodes(nodes_input, generated_nodes_positions,10, nodes_offset)
    draw_connections(nodes_input, generated_nodes_positions, directed_input,
                     nodes_offset)
    draw_legend([200, -200])
    finish_drawing()
