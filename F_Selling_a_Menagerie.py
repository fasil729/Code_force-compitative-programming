from collections import defaultdict


def topological_sort(graph):
    # Count the incoming edges for each vertex
    incoming_edges = {v: 0 for v in graph}

    # Calculate the incoming edges for each vertex
    for vertex in graph:
        for neighbor in graph[vertex]:
            incoming_edges[neighbor] += 1

    # Initialize an empty list to store the sorted vertices
    sorted_vertices = []

    # Collect vertices with no incoming edges
    no_incoming_edges = [v for v in graph if incoming_edges[v] == 0]

    # Perform topological sorting
    while no_incoming_edges:
        # Remove a vertex with no incoming edges
        vertex = no_incoming_edges.pop()
        sorted_vertices.append(str(vertex))

        # Update the incoming edges of the neighbors
        for neighbor in graph[vertex]:
            incoming_edges[neighbor] -= 1
            if incoming_edges[neighbor] == 0:
                no_incoming_edges.append(neighbor)

    # Check for a cycle
    if len(sorted_vertices) != len(graph):
        return None  # Graph contains a cycle

    return sorted_vertices

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(n):
        graph[i + 1].append(a[i])
    ans = topological_sort(graph)
    print(ans)
    print((ans))