def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    temp = graph[start] - visited
    for next in temp:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['4']),
         '1': set(['2', '4']),
         '2': set(['1', '3', '4']),
         '3': set(['2']),
         '4': set(['0', '1', '2'])}

dfs(graph, '0')