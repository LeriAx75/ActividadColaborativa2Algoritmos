from collections import deque


def bfs(rGraph, s, t, parent):
    visited = [False] * len(rGraph)
    q = deque()
    q.append(s)
    visited[s] = True
    parent[s] = -1

    while q:
        u = q.popleft()
        for v in range(len(rGraph)):
            if not visited[v] and rGraph[u][v] > 0:
                q.append(v)
                parent[v] = u
                visited[v] = True
    return visited[t]


def fordFulkerson(graph, s, t):
    V = len(graph)
    rGraph = [row[:] for row in graph]
    parent = [-1] * V
    max_flow = 0

    while bfs(rGraph, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, rGraph[u][v])
            v = parent[v]

        v = t
        while v != s:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow
