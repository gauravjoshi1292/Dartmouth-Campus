from collections import deque
import PyQt4

def breadth_first_search(start, goal):
    """
    Function that returns the path from start to goal
    :param start: Start Vertex
    :param goal: Destination vertex
    :return: List containing the path from start vertex to goal vertex
    """
    # Dictionaries containing back pointers and distance from the start
    back_pointers = {}
    distance = {}

    # FIFO queues that stores vertices
    queue = deque()

    # Initialization
    back_pointers[start] = None
    distance[start] = 0
    queue.append(start)

    # Visit all the vertices one by one
    while queue:
        s = queue.popleft()

        # Visit all adjacent vertices
        for v in s.adjacent_vertices:
            d = 0
            try:
                # If the adjacent vertex already has a back pointer,
                # Check if the new distance is less than the current one, if so update the distance and the back pointer
                back_pointers[v]
                d = 1 + distance[s]
                if d < distance[v]:
                    distance[v] = d
                    back_pointers[v] = s
            except KeyError:
                # If there's no back pointer and the vertex is not start vertex, add a back pointer and a distance
                if v != start:
                    queue.append(v)
                    back_pointers[v] = s
                    distance[v] = distance[s] + 1

    # List that will contain all the vertices in the path
    path = []
    begin = goal

    # Start from the goal and trace all the way back until you reach the start vertex
    while begin:
        path.append(begin)
        begin = back_pointers[begin]

    # Reverse the path
    path.reverse()
    return path