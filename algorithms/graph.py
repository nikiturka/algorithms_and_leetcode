import heapq
from collections import deque

my_graph = {
    1: [(2, 1), (3, 4)],
    2: [(1, 1), (3, 2), (4, 5)],
    3: [(1, 4), (2, 2), (4, 1)],
    4: [(2, 5), (3, 1)]
}


def bfs(graph: dict, start: int) -> list[int]:
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return result


def dfs(graph: dict, start: int, visited: set = None) -> list[int]:
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result


def dijkstra(graph: dict, start: int) -> dict:
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
