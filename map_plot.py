from cs1lib import *
from load_graph import load_graph
from bfs import breadth_first_search


# The lower left corner of the window has a pixel value (0, 0) and the upper right corner has a pixel value (740, 380)
# The lower left corner of the map has a pixel value (10, 10) and the upper right corner has a pixel value (730, 370)
# I have added a padding of 10px either side for the map inside the window


WINDOW_WIDTH = 1012  # Width of the graphics window in pixels
WINDOW_HEIGHT = 811  # Height of the graphics window in pixels
MAP_WIDTH = 1012.0  # Map width in pixels
MAP_HEIGHT = 811.0  # Map height in pixels


def draw_red_vertex():
    """
    Function that draws a red vertex,  it is called when the mouse button is pressed
    :return: None
    """
    disable_stroke()
    x = mouse_x()
    y = mouse_y()
    enable_fill()
    set_fill_color(1, 0, 0)
    draw_circle(x, y, 7)
    enable_stroke()


def draw_map():
    """
    Draws the map on the graphics window and plots the campus paths connecting various locations
    :return: None
    """

    # Load the image
    img = load_image("dartmouth_map.png")  # Load the image

    # Get the vertex dictionary
    vertex_dict = load_graph("dartmouth_graph.txt")

    # Enable smoothing
    enable_smoothing()

    # Draw the image
    draw_image(img, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, MAP_WIDTH/2, MAP_HEIGHT/2)

    # Draw the map with blue vertices and edges
    for v in vertex_dict.values():
        enable_fill()
        v.draw_vertex(0, 0, 1)
        for u in v.adjacent_vertices:
            v.draw_edge(u, 0, 0, 1)

    # Initialize start
    start = None

    # Keep waiting until mouse button is pressed, If the button is pressed on a vertex make that vertex the start vertex
    while not mouse_down():
        if window_closed():
            cs1_quit()
        set_mouse_button_function(draw_red_vertex)
        sx = mouse_x()
        sy = mouse_y()
        for v in vertex_dict.values():
            if v.is_goal(sx, sy):
                start = v
        request_redraw()

    if window_closed():
        cs1_quit()
    # Draw the paths to the vertices on which the mouse hovers
    while not window_closed():
        # Initialize goal
        goal = None

        # Find a vertex if it lies in the surrounding square
        for v in vertex_dict.values():
            if v.is_goal(mouse_x(), mouse_y()):
                goal = v
                break

        # If we have a start and a goal vertex, get the bfs path and draw the path in red color
        if start:
            enable_stroke()
            set_stroke_width(1)
            set_font_size(10)
            set_stroke_color(0, 0, 0)
            # Show the name of starting vertex
            draw_text(start.name, start.x - 20, start.y - 10)
            disable_stroke()

        if window_closed():
            cs1_quit()

        if start and goal:
            enable_stroke()
            set_stroke_color(0, 0, 0)

            # Show the name of goal vertex
            if goal != start:
                draw_text(goal.name, goal.x - 20, goal.y - 10)
            disable_stroke()

            # Do bfs, get the path
            path = breadth_first_search(start, goal)

            # Draw the path
            for i in range(1, len(path)):
                disable_stroke()
                enable_fill()
                path[i].draw_vertex(1, 0, 0)
                disable_fill()
                enable_stroke()
                path[i-1].draw_edge(path[i], 1, 0, 0)

        if window_closed():
            cs1_quit()

        # Redraw
        request_redraw()

    # Quit the graphics window
    if window_closed():
        cs1_quit()


def draw_window():
    """
    Draws the graphics window and calls the draw_map function that draws the dartmouth map
    :return: None
    """
    start_graphics(draw_map, "Dartmouth Map", WINDOW_WIDTH, WINDOW_HEIGHT)


draw_window()