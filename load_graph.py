from vertex import Vertex


def load_graph(file_name="dartmouth_graph.txt"):
    """

    :param file_name: input file name
    :return: dictionary containing all the vertex name as key with a vertex object as value
    """
    data = []
    # Dictionary that will contain all the vertices
    vertex_dict = {}
    with open(file_name) as file:
        # First pass, read the file line by line and add key and vertex object to the dictionary
        for line in file:
            data.append(line)
            name = str(line.split("; ")[0])
            coordinates = line.split("; ")[2]
            x = int(coordinates.split(", ")[0])
            y = int(coordinates.split(", ")[1])
            new_vertex = Vertex()
            new_vertex.name = name
            new_vertex.x = x
            new_vertex.y = y
            new_vertex.adjacent_vertices = []
            vertex_dict[name] = new_vertex

    for line in data:
        # Second pass, add vertex object to adjacency list
        name = str(line.split("; ")[0])
        adjacent_string = line.split("; ")[1]
        adjacency_list = adjacent_string.split(", ")
        for vertex in adjacency_list:
            vertex_dict[name].adjacent_vertices.append(vertex_dict[vertex])

    return vertex_dict