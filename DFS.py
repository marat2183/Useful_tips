def dfs(start, visited, prev, g):
    print(start)
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)
            print(start)


g = [[4], [2, 4], [1, 3, 4], [2], [0, 1, 2]]
visited = [False] * len(g)
prev = [None] * len(g)
start = 3
dfs(start, visited, prev, g)
