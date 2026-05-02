try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Error: networkx or matplotlib not installed. Install with: pip install networkx matplotlib")
    print(f"Details: {e}")
    nx = None
    plt = None

# Your graph
graph = {
#add your (code) graph here as a dictionary
'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []




}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph.get(node, []) if n not in visited and n not in queue])
    return visited


def dfs(graph, start):
    visited = []

    def _dfs(node):
        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                _dfs(neighbor)

    _dfs(start)
    return visited


def dls(graph, start, depth):
    visited = []

    def _dls(node, current_depth):
        if current_depth < 0 or node in visited:
            return
        visited.append(node)
        if current_depth == 0:
            return
        for neighbor in graph.get(node, []):
            _dls(neighbor, current_depth - 1)

    _dls(start, depth)
    return visited


def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, depth)
        if result:
            return result
    return []


# Create directed graph and draw if dependencies available
if nx is not None and plt is not None:
    G = nx.DiGraph()

    # Add edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw
    plt.figure(figsize=(6, 5))
    pos = nx.spring_layout(G)  # auto layout

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=12,
        font_weight='bold',
        arrows=True
    )

    plt.title("Graph Representation")
    plt.show()

print("BFS:",bfs(graph, 'A')) #add function calls with their respective arguments
print("DFS:",dfs(graph, 'A')) #add function calls with their respective arguments
print("IDDFS:",iddfs(graph, 'A', 3)) #add function calls with their respective arguments