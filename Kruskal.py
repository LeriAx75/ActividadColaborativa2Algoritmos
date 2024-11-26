def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskalMST(graph):
    result = []
    i, e = 0, 0
    edges = []
    V = len(graph)

    # Crear una lista de aristas a partir de la matriz de adyacencia
    for u in range(V):
        for v in range(V):
            if graph[u][v] != 0:
                edges.append((graph[u][v], u, v))

    # Ordenar aristas por peso
    edges.sort(key=lambda x: x[0])
    parent, rank = [], []
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Construir el MST
    mst_cost = 0
    while e < V - 1:
        w, u, v = edges[i]
        i += 1
        x, y = find(parent, u), find(parent, v)

        # Si no forma un ciclo, incluirla en el MST
        if x != y:
            e += 1
            result.append((u, v))
            mst_cost += w
            union(parent, rank, x, y)

    return result, mst_cost
