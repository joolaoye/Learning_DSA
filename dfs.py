def DFS(graph,source):
    stack = [source]
    explored = []

    while stack:
        cur = stack.pop()
        explored.append(cur)

        stack += graph[cur]

    return explored


def recursive_DFS(graph, source,explored=None):
    if explored is None:
        explored = []

    if source in explored:
        return

    neighbours = graph[source]
    explored.append(source)

    for nodes in neighbours:
        recursive_DFS(graph,nodes,explored)

    return explored


graph = {
    'a': ['b'],
    'b': ['d'],
    'c': ['a'],
    'd':['f'],
    'e':['c'],
    'f':['e']

}


print(recursive_DFS(graph,'a'))