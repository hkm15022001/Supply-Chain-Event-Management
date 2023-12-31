def dijkstra_shortest_path(graph, start_location):
    unvisited_queue = []
    for v in graph.adjacency_list:
        unvisited_queue.append(v)

    start_location.distance = 0

    while len(unvisited_queue) > 0:
        smallest = 0

        for e in range(1, len(unvisited_queue)):
            if unvisited_queue[e].distance < unvisited_queue[smallest].distance:
                smallest = e

        current_location = unvisited_queue.pop(smallest)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in graph.adjacency_list[current_location]:

            edge_weight = graph.edge_weights[(current_location, adj_vertex)]
            alternative_path_distance = current_location.distance + edge_weight
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.predecessor = current_location


# Start from end_vertex and build the path backwards.
def get_shortest_path(start_location, end_location):
    path = ''
    current_location = end_location
    while current_location is not start_location:
        if current_location is None:
            break
        # print("destination: ", current_location.label, "predecessor: ", current_location.predecessor, "distance: ", current_location.distance)
        path = " -> " + str(current_location.label) + path
        current_location = current_location.predecessor
    path = start_location.label + path
    return path
