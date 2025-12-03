import math
import turtle as turtle
from copy import deepcopy


def calculate_outgoing_degree(knot_in, knots_in):
    """Calculates the outgoing degree of a knot."""
    connections = knots_in[knot_in]
    return len(connections)+1

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
    angle = math.degrees(math.atan2(end_position[1] - start_position[1], end_position[0] - start_position[0]))
    return angle

def draw_knot(knot, position, color, size, offset=(0,0)):
    """Draws a single knot at a given position."""
    print(f"Drawing Knot: ({knot}) at position: {position[0]+offset[0]}, "
          f"{position[1]+offset[1]} with color: {color}")
    turtle.teleport(position[0]+offset[0], position[1]+offset[1])
    turtle.dot(size, color)
    turtle.write(knot)

def draw_connection(start_position, end_position, directional=False, offset=(0,0)):
    """Draws a connection between two knots."""
    angle = calculate_angle(start_position, end_position)
    print(f"Drawing Connection from: {start_position} to: {end_position}")
    turtle.teleport(start_position[0]+offset[0], start_position[1]+offset[1])
    turtle.setheading(angle)
    turtle.pendown()
    turtle.goto(end_position[0]+offset[0], end_position[1]+offset[1])
    if directional:
        turtle.stamp()
    turtle.penup()

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
    turtle.hideturtle()
    turtle.done()

def draw_knots(knots_in, knots_positions_in, size=10, offset=(0,0)):
    """Draws a dict of knots at given positions."""
    turtle.tracer(0)
    for knot in knots_in:
        position = knots_positions_in[knot]
        color = get_knot_color(knot, knots_in)
        draw_knot(knot, position, color, size, offset)
    turtle.update()

def draw_connections(knots_in, knots_positions_in, directional=False, offset=(0,0)):
    """Draws connections between knots."""
    turtle.tracer(1)
    for knot in knots_in:
        start_position = knots_positions_in[knot]
        connections = knots_in[knot]
        for connected_knot in connections:
            end_position = knots_positions_in[connected_knot]
            draw_connection(start_position, end_position, directional, offset)

def draw_legend(position=(200,200), offset=20):
    """Draws a legend for the knot colors."""
    turtle.tracer(0)
    turtle.teleport(position[0], position[1])
    turtle.write("Legend:")
    turtle.teleport(position[0], position[1]-offset)
    turtle.dot(10, "red")
    turtle.write(" Knoten mit Ausgangsgrad 1")
    turtle.teleport(position[0], position[1]-(2*offset))
    turtle.dot(10, "green")
    turtle.write(" Knoten mit Eingangsgrad 0")
    turtle.teleport(position[0], position[1]-(3*offset))
    turtle.dot(10, "blue")
    turtle.write(" Knoten mit sonstigen Graden")
    turtle.update()
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
    else:
        return False

def append_knot(knot_in, knots_in):
    """Appends a new knot to the knots dictionary."""
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
    cols = math.ceil(math.sqrt(len(knots_in)))

    positions = []
    for i in range(len(knots_in)):
        row = i // cols
        col = i % cols
        positions.append((col * distance, row * distance))
    return positions

def input_handler():
    """Handles user input for graph configuration."""
    directed = None
    while directed is None:
        input_string = input("Directed or Undirected graph? (y/n): ").lower()
        if input_string == 'y':
            directed = True
        elif input_string == 'n':
            directed = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            directed = None

    option = None
    print("Input Knots:")
    print("Options:")
    print("1. Automatically Generate Knots")  #TODO Automatically generate knots Function
    print("2. Input Knots Manually (as a valid list like 1,2,3...)")
    print("3. Input Knot Positions Manually (as a valid dict like: {Knot_Name: (x_position, y_position)})")
    while option is None:
        input_string = input("Option 1/2/3/4) >")
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

    connections = None
    print("Setup Knot-Connections:")
    print("4. Set Knot Connections (as a valid dict like: "
          "{Knot_Name: (Connected_Knot1, Connected_Knot2, ...), Knot_Name2: (...), ...})")
    while connections is None:
        input_string = input("Connections >")


#print(check_edge_count(knots, True))

if __name__ == '__main__':

    input_handler()

    knots = {
        0: (1, 2, 3),
        1: (4,),
        2: (5,),
        3: (6,),
        4: (7,),
        5: (8,),
        6: (),
        7: (9,),
        8: (),
        9: ()
    }

    knots_positions = generate_knot_positions(knots, 50)
    turtle.setup(1000,1000)
    turtle.speed(0)

    knots_offset = [0, 0]

    draw_knots(knots, knots_positions, 10, knots_offset)
    draw_connections(knots, knots_positions, True, knots_offset)
    draw_legend([200,-200])
    finish_drawing()
