a, b, c, d, e = range(5)
N = [
	{b:1, d:4}, # a
	{a:1, c:10}, # b
	{b:10, d:5, e:1}, # c
	{a:4, c:5, e:2}, # d
    {c:1, d:2} #e
]
start = d
INF = 10 ** 10
n = 5
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in N[i].keys():
        if dist[i] + N[i][j] < dist[j]:
            dist[j] = dist[i] + N[i][j]
    min_dist = INF
    for j in N[i].keys():
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
for i in range(len(dist)):
    itog = f'Расстояние от вершины {start} до вершины {i} = {dist[i]}'
    print(itog)