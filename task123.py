import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

social_network = nx.Graph()

social_network.add_nodes_from([1, 2, 3, 4, 5, 6])

social_network.add_edges_from(
    [
        (1, 2, {"weight": 2}),
        (1, 3, {"weight": 1}),
        (2, 4, {"weight": 3}),
        (3, 5, {"weight": 2}),
        (4, 6, {"weight": 1}),
        (5, 6, {"weight": 2}),
        (1, 4, {"weight": 1}),
        (1, 5, {"weight": 2}),
        (2, 3, {"weight": 1}),
        (4, 5, {"weight": 2}),
        (2, 6, {"weight": 3}),
    ]
)

pos = nx.spring_layout(social_network)
nx.draw(
    social_network,
    pos,
    with_labels=True,
    font_weight="bold",
    node_size=700,
    node_color="skyblue",
    font_size=10,
    font_color="black",
    edge_color="gray",
)
plt.title("Соціальна мережа")

# Аналіз основних характеристик
print("Кількість вершин:", social_network.number_of_nodes())
print("Кількість ребер:", social_network.number_of_edges())
print("Список ступенів вершин:", dict(social_network.degree()))


def dfs(graph, start, path=[]):
    path = path + [start]
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            path = dfs(graph, neighbor, path)
    return path


def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph.neighbors(node))
    return visited


for method in (dfs, bfs):
    for vertex in list(social_network.nodes):
        print(f"{method.__name__} | {vertex} | ", end="")
        print(*method(social_network, vertex), sep=" ")
    print()


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Застосування алгоритму Дейкстри для кожної вершини
for vertex in social_network.nodes:
    shortest_paths = dijkstra(social_network, vertex)
    print(f"Найкоротші шляхи від вершини{vertex}: {shortest_paths}")

plt.show()
