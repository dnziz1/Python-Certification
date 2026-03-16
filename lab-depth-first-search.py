def dfs(matrix, node):
    visited = [False] * len(matrix)
    result = []
    stack = [node]

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True
            result.append(current)
        
        for neighbor in range(len(matrix) - 1, -1, -1):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                stack.append(neighbor)

    return result

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))
