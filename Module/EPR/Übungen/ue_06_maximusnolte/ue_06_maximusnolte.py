import math
import turtle as t
from copy import deepcopy


def calculate_outgoing_degree(knot_in, knots_in):
    """Calculates the outgoing degree of a knot.
    """
    connections = knots_in[knot_in]
    return len(connections) + 1


def calculate_incoming_degree(knot_in, knots_in):
    """Calculates the incoming degree of a knot."""
    count = 0
    for k in knots_in:
        connections = knots_in[k]
        if knot_in in connections:
            count += 1
    return count


def calculate_angle(start_position, end_position):
    """Calculates the angle between two positions."""
    angle = math.degrees(math.atan2(end_position[1] - start_position[1],
                                    end_position[0] - start_position[0]))
    return angle


def draw_knot(knot, position, color, size, offset=(0, 0)):
    """Draws a single knot at a given position."""
    print(f"Drawing Knot: ({knot}) at position: {position[0] + offset[0]}, "
          f"{position[1] + offset[1]} with color: {color}")
    t.teleport(position[0] + offset[0], position[1] + offset[1])
    t.dot(size, color)
    t.write(knot)


def draw_connection(start_position, end_position, directional=False,
                    offset=(0, 0)):
    """Draws a connection between two knots."""
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


def get_knot_color(knot_in, knots_in):
    """Determines the color of a knot based on its degrees."""
    outgoing_degree = calculate_outgoing_degree(knot_in, knots_in)
    incoming_degree = calculate_incoming_degree(knot_in, knots_in)
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


def draw_knots(knots_in, knots_positions_in, size=10, offset=(0, 0)):
    """Draws a dict of knots at given positions."""
    t.tracer(0)
    for knot in knots_in:
        position = knots_positions_in[knot]
        color = get_knot_color(knot, knots_in)
        draw_knot(knot, position, color, size, offset)
    t.update()


def draw_connections(knots_in, knots_positions_in, directional=False,
                     offset=(0, 0)):
    """Draws connections between knots."""
    t.tracer(1)
    for knot in knots_in:
        start_position = knots_positions_in[knot]
        connections = knots_in[knot]
        for connected_knot in connections:
            end_position = knots_positions_in[connected_knot]
            draw_connection(start_position, end_position, directional, offset)


def draw_legend(position=(200, 200), offset=20):
    """Draws a legend for the knot colors."""
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


def calculate_edge_count(knots_in, directed=False):
    """Calculates the number of edges in the graph."""
    if directed:
        edge_count = 0
        for knot in knots_in:
            connections = knots_in[knot]
            edge_count += len(connections)
        return edge_count

    edge_count = 0
    for neighbors in knots_in.values():
        edge_count += len(neighbors)
    return edge_count // 2


def check_edge_count(knots_in, directed=False):
    """Checks if the edge count matches the expected value for a tree."""
    edge_count = calculate_edge_count(knots_in, directed)
    if edge_count == len(knots_in) - 1:
        return True
    return False


def append_knot(knot_in, knots_in):
    """Appends a new knot to the knots dictionary."""
    knot_in = str(knot_in)
    if knot_in not in knots_in:
        knot_in = {knot_in: ()}
        knots_in.update(knot_in)
        return knots_in
    return None


def set_knot_connections(knot_in, knots_in, new_connections):
    """Sets new connections for a given knot."""
    if knot_in in knots_in:
        knots_in[knot_in] = new_connections
        return knots_in
    return None


def generate_knot_positions(knots_in, distance=100):
    """Generates positions for knots in a grid layout."""
    print("Generating positions for knots...")
    cols = math.ceil(math.sqrt(len(knots_in)))

    positions = {}
    for i, knot in enumerate(knots_in):
        row = i // cols
        col = i % cols
        positions.update({knot : (col * distance, row * distance)})
    print(f"Finished generating positions for knots. Positions: {positions}")
    return positions


def convert_string_connections(input_string, knots):
    """Converts a string representation of connections into a dict."""
    print("Converting string to connections...")

    input_string = input_string.strip()
    if ";" not in input_string:
        print("Invalid input format. Please separate entries with semicolons.")
        return None

    entries = input_string.split(';')

    for entry in entries:
        if entry == "":
            continue
        if ":" not in entry or entry.count(":") != 1:
            print(f"Invalid entry: {entry}")
            return None

        knot, connected_knots_raw = entry.split(":")

        connected_knots_raw = connected_knots_raw.split(",")
        connected_knots = []
        for connection in connected_knots_raw:
            if connection != "":
                connected_knots.append(connection)

        connected_knots = tuple(connected_knots)

        if knot not in knots:
            print(f"Knot {knot} does not exist.")
            return None

        knots[knot] = connected_knots

    print("Converted connections:")
    print(knots)
    return knots


def generate_knot_dict(number_of_knots):
    """Generates a dictionary of knots with no connections."""
    knots = {}
    for i in range(number_of_knots):
        append_knot(i+1, knots)
    return knots


def option_handler(option):
    """Handles user options for knot input."""
    match option:
        case 1:
            print("How many knots to generate?")
            number_of_knots = 0
            while number_of_knots == 0:
                input_string = input("Number of Knots >")
                try:
                    input_string = int(input_string)
                    if input_string > 0:
                        number_of_knots = deepcopy(input_string)
                    else:
                        print(
                            "Invalid input. Please enter a positive integer.")
                        number_of_knots = 0
                except ValueError, TypeError:
                    print("Invalid input. Please enter a positive integer.")
                    number_of_knots = 0
            return generate_knot_dict(number_of_knots)
        case 2:
            print("Input knots manually as a valid list like K1,K2,K3...")
            knots = None
            while knots is None:
                input_string = input("Knots >")
                if ";" in input_string:
                    entries = input_string.split(';')
                    knots = {}
                    for entry in entries:
                        entry = entry.strip()
                        if entry != "":
                            append_knot(entry, knots)
                else:
                    print(
                        "Invalid input format. Please separate entries with semicolons.")
                    knots = None
            return knots
        case 3:
            print("Input knot positions manually as a valid dict like: "
                  "x_position, y_position; separated by"
                  "semicolons, Knot Names will be auto-generated")
            knots = None
            while knots is None:
                knots = {}
                input_string = input("Knot Positions >")
                if ";" in input_string:
                    entries = input_string.split(';')
                    for i, entry in enumerate(entries):
                        entry = entry.strip().split(",")
                        if entry == ['']:
                            continue
                        else:
                            if len(entry) != 2:
                                print(f"Invalid entry (must have exactly two values): {entry}")
                                knots = None
                                break
                            x_position = entry[0]
                            y_position = entry[1]
                            if x_position.isdigit() and y_position.isdigit():
                                append_knot(i, knots)
                                set_knot_connections(i, knots, (int(x_position), int(y_position)))
                                print(f"Added knot {i} with position ({x_position}, {y_position})")
                            else:
                                print(f"Invalid entry ({x_position}, "
                                  f"{y_position}): {entry} got non -integer values")
                                knots = None
                else:
                    print(
                        "Invalid input format. Please separate entries with semicolons.")
                    knots = None
            return knots
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
    # Setting up knots
    option = None
    print("----Input Knots----")
    print("Options:")
    print(
        "1. Automatically Generate Knots")
    print(
        "2. Input Knots Manually (as a valid list like 1,2,3...), seperated by semicolons")
    print(
        "3. Input Knot Positions Manually (as a valid dict like: Knot_Name: x_position, y_position); separated by semicolons, Knot Names will be auto-generated")
    while option is None:
        input_string = input("Option 1/2/3) >")
        try:
            input_string = int(input_string)
            if input_string in [1, 2, 3, 4]:
                option = deepcopy(input_string)
            else:
                print("Invalid input. Please enter '1', '2', '3' or '4'.")
                option = None
        except ValueError, TypeError:
            print("Invalid input. Please enter '1', '2', '3' or '4'.")
            option = None
    knots = option_handler(option)

    # Setting up connections
    connections = None
    print("----Setup Knot-Connections----")
    print("Set Knot Connections (as a valid dict like: "
          "Knot_Name: Connected_Knot1, Connected_Knot2, ...; separated by semicolons)")
    while connections is None:
        input_string = input("Connections >")
        connections = convert_string_connections(input_string, knots)
    knots = connections

    print("----FinalResult----")
    print(directed, knots)
    return directed, knots


if __name__ == '__main__':
    directed_input, knots_input = input_handler()
    generated_knots_positions = generate_knot_positions(knots_input, 100)

    t.setup(1000, 1000)
    t.speed(0)

    knots_offset = [0, 0]

    draw_knots(knots_input, generated_knots_positions, 10, knots_offset)
    draw_connections(knots_input, generated_knots_positions, directed_input,
                     knots_offset)
    draw_legend([200, -200])
    finish_drawing()
