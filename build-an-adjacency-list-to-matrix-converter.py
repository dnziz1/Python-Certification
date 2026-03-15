def adjacency_list_to_matrix(graph):
    n = len(graph)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix

print(adjacency_list_to_matrix({0: [1], 1: [0]}))
print(adjacency_list_to_matrix({0: [], 1: [], 2: []}))
