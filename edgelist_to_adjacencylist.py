def convert_to_adjList(edge_list):
    graph = {}

    for pairs in edge_list:
        x,y = pairs

        if x not in graph:
            graph[x] = [y]
        else:
            graph[x].append(y)

        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)


    return graph

Edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]


print(convert_to_adjList(Edges))