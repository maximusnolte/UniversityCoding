__author__ = '8722674, Julian Maximus Nolte'
#! /venv/bin/python3.14

import turtle as t
import random as rnd
import time

def reset():
    """Wird benötigt um das Turtle-Fenster zurückzusetzen nach Abschluss des Programms."""
    t.TurtleScreen._RUNNING = True
    try:
        t.bye()
    except:
        pass

def dreieckFraktal(iterations, size=100, position=(0, 0), start_position=(0, 0)):
    """
    Zeichnet ein Sierpinski-Dreieck mithilfe des Chaos-Game-Verfahrens.

    Parameter:
        iterations (int): Anzahl der Berechnungsschritte für das Fraktal.
        size (int): Seitenlänge des gleichseitigen Dreiecks.
        position (tuple): Punkt, der nach Abschluss markiert wird.
        start_position (tuple): Verschiebung des gesamten Dreiecks.

    Die Funktion erzeugt ein Turtle-Fenster, berechnet die Dreiecksecken,
    führt das Chaos-Game aus und setzt anschließend die Turtle-Umgebung zurück.
    """
    print(f"Triangle Fractal with {iterations} iterations, size = {size}, position = {position}, start_position = {start_position}")
    height = size*1.73205080757/2
    corners = []
    t.setup(1000,1000)
    root = t.getcanvas().winfo_toplevel()
    root.lift()
    root.attributes('-topmost', True)
    def on_close():
        print("Closing Window...")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    t.speed(0)
    t.tracer(0)
    t.up()
    t.setposition(0+start_position[0],(height/2)+start_position[1])

    corners.append(t.position())
    t.dot(5, "red")
    print(f"1. Corner at {corners[0]}")

    # rechte Ecke
    t.setposition(size/2+start_position[0], -height/2+start_position[1])
    corners.append(t.position())
    t.dot(5,"red")
    print(f"2. Corner at {corners[1]}")

    # linke Ecke
    t.setposition(-size/2+start_position[0], -height/2+start_position[1])
    corners.append(t.position())
    t.dot(5, "red")
    print(f"3. Corner at {corners[2]}")

    print(f"Starting Fractal with {iterations} iterations...")
    start_time = time.time()
    for i in range(iterations):
        target_pos= rnd.choice(corners)
        half_pos = ((t.position()[0] + target_pos[0])/2, (t.position()[1] + target_pos[1])/2)
        t.setposition(half_pos)
        t.dot(2, "blue")
    t.setposition(position)
    t.dot(10, "green")
    t.hideturtle()
    t.update()
    print(f"Finished in...{time.time()-start_time}s")
    t.done()
    reset()
    return True