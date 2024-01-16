def BFS(graph,source):
    queue = [source]

    explored = []

    while queue:
        cur = queue.pop(0)

        if cur not in explored:

            explored.append(cur)

            queue += graph[cur]

    return explored


graph = {
    'a': ['b'],
    'b': ['d'],
    'c': ['a'],
    'd':['f'],
    'e':['c'],
    'f':['e']

}

print(BFS(graph,'a'))