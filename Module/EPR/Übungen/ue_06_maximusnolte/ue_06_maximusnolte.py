import math
import turtle as turtle

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
knots_positions = {

    0: (250, 300),



    1: (100, 180),

    2: (250, 180),

    3: (400, 180),



    4: (60,  60),

    5: (200, 60),

    6: (340, 60),



    7: (100, -60),

    8: (400, -60),
    


    9: (250, -180)

}
def calculate_outgoing_degree(knot_in, knots_in):
    connections = knots_in[knot_in]
    return len(connections)+1

def calculate_incoming_degree(knot_in, knots_in):
    count = 0
    for k in knots_in:
        connections = knots_in[k]
        if knot_in in connections:
            count += 1
    return count

def calculate_angle(start_position, end_position):
    angle = math.degrees(math.atan2(end_position[1] - start_position[1], end_position[0] - start_position[0]))
    return angle

def draw_knot(knot, position, color, size, offset=(0,0)):
    print(f"Drawing Knot: ({knot}) at position: {position[0]+offset[0]}, {position[1]+offset[1]} with color: {color}")
    turtle.teleport(position[0]+offset[0], position[1]+offset[1])
    turtle.dot(size, color)
    turtle.write(knot)

def draw_connection(start_position, end_position, directional=False, offset=(0,0)):
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
    outgoing_degree = calculate_outgoing_degree(knot_in, knots_in)
    incoming_degree = calculate_incoming_degree(knot_in, knots_in)
    if outgoing_degree == 1:
        return "red"
    elif incoming_degree == 0:
        return "green"
    else:
        return "blue"

# Draw connections
def finish_drawing():
    turtle.hideturtle()
    turtle.done()

def draw_knots(knots_in, knots_positions_in, size=10, offset=(0,0)):
    turtle.tracer(0)
    for knot in knots_in:
        position = knots_positions_in[knot]
        color = get_knot_color(knot, knots_in)
        draw_knot(knot, position, color, size, offset)
    turtle.update()

def draw_connections(knots_in, knots_positions_in, directional=False, offset=(0,0)):
    turtle.tracer(1)
    for knot in knots_in:
        start_position = knots_positions_in[knot]
        connections = knots_in[knot]
        for connected_knot in connections:
            end_position = knots_positions_in[connected_knot]
            draw_connection(start_position, end_position, directional, offset)

def draw_legend(position=(200,200), offset=20):
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
    if directed:
        edge_count = 0
        for knot in knots_in:
            connections = knots_in[knot]
            edge_count += len(connections)
        return edge_count
    else:
        edge_count = 0
        for neighbors in knots_in.values():
            edge_count += len(neighbors)
        return edge_count // 2

def check_edge_count(knots_in, directed=False):
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

def knot_input_handeler():
    directed = None
    while directed is None:
        input_string = input("Directed or Undirected graph? (y/n): ").strip().lower()
        if input_string == 'y':
            directed = True
        elif input_string == 'n':
            directed = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            directed = None



#print(check_edge_count(knots, True))

if __name__ == '__main__':


    pass
    #knots_positions = generate_knot_positions(knots, 50)
    #turtle.setup(1000,1000)
    #turtle.speed(0)

    #offset = [0, 0]

    #draw_knots(knots, knots_positions, 10, offset)
    #draw_connections(knots, knots_positions, True, offset)
    #draw_legend([200,-200])
    #finish_drawing()