def dfs(start, visited, prev, graph):
    print(start)
    visited[start] = True
    for u in graph[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, graph)
            print(start)


graph = [[4], [2, 4], [1, 3, 4], [2], [0, 1, 2]]
visited = [False] * len(graph)
prev = [None] * len(graph)
start = 0
dfs(start, visited, prev, graph)
