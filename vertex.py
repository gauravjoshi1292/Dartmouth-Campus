from cs1lib import *

# Constants that are used to set the radius of circle, width of an edge and the dimensions of the surrounding square
RED_RADIUS = 7
BLUE_RADIUS = 5
EDGE_WIDTH = 3
SQUARE_WIDTH = 10
SQUARE_HEIGHT = 10


class Vertex:
    """
    Vertex class that contains all the information for a vertex
    """
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent_vertices = []

    def __str__(self):
        """
        :return: string representation for the vertex
        """
        retVal = self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: "

        for v in self.adjacent_vertices:
            retVal += str(v.name) + ", "
        retVal = retVal.rstrip(", ")
        return retVal

    def draw_vertex(self, r, g, b):
        """
        Draw a circle corresponding to the verex
        :param r: red
        :param g: green
        :param b: blue
        :return: none
        """
        set_fill_color(r, g, b)
        if b == 1:
            draw_circle(self.x, self.y, BLUE_RADIUS)
        if r == 1:
            draw_circle(self.x, self.y, RED_RADIUS)
        disable_fill()

    def draw_edge(self, destination, r, g, b):
        """
        Draw an edge between two vertices
        :param destination: destination vertex
        :param r: red
        :param g: green
        :param b: blue
        :return: none
        """
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, destination.x, destination.y)

    def is_goal(self, x, y):
        """
        Returns True if the point lies inside the smallest surrounding the vertex
        :param x: x coordinate of the mouse
        :param y: y coordinate of the mouse
        :return: boolean
        """
        width = SQUARE_WIDTH
        height = SQUARE_HEIGHT
        min_x = self.x - width
        max_x = self.x + width
        min_y = self.y - height
        max_y = self.y + height
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            return True
        else:
            return False
