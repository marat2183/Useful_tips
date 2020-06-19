def BFS(start, V, D):
    D[start] = 0
    Q = [start]
    Qstart = 0
    while Qstart < len(Q):
        u = Q[Qstart]
        print(u)
        Qstart += 1
        for v in V[u]:
            if D[v] is None:
                D[v] = D[u] + 1
                Q.append(v)


g = [[4], [2, 4], [1, 3, 4], [2], [0, 1, 2]]
D = [None] * (len(g) + 1)
BFS(1, g, D)
