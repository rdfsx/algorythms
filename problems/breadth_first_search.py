def bfs(n, m, edges, s):
    """
    :param n: number of nodes
    :param m: number of edges
    :param edges: edges list
    :param s: starting node
    :return:
    """
    graph = {}
    for n1, n2 in edges:
        if not graph.get(n1):
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)
        if not graph.get(n2):
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)
    que = [s]
    distances = [-1] * n
    distances[s - 1] = 0
    while que:
        current_node = que.pop(0)
        for neighbor in graph[current_node]:
            if distances[neighbor - 1] == -1:
                que.append(neighbor)
                distances[neighbor - 1] = distances[current_node - 1] + 6
    distances.remove(0)
    return distances


def bfs2(n, m, edges, s):
    graph = {}
    for n1, n2 in edges:
        if not graph.get(n1):
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)

        if not graph.get(n2):
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)

    que = [s]
    distances = [-1] * n
    distances[s - 1] = 0

    while que:
        current_node = que.pop(0)
        for neighbour in graph[current_node]:
            if distances[neighbour - 1] == -1:
                que.append(neighbour)
                distances[neighbour - 1] = distances[current_node - 1] + 6
    distances.remove(0)
    return distances


if __name__ == "__main__":
    edges = [[1, 2], [1, 3]]
    m = 2
    n = 4
    s = 1

    print(bfs2(n, m, edges, s))

    # q = int(input().strip())
    #
    # for q_itr in range(q):
    #     first_multiple_input = input().rstrip().split()
    #
    #     n = int(first_multiple_input[0])
    #
    #     m = int(first_multiple_input[1])
    #
    #     edges = []
    #
    #     for _ in range(m):
    #         edges.append(list(map(int, input().rstrip().split())))
    #
    #     s = int(input().strip())
    #
    #     result = bfs(n, m, edges, s)
    #
    #     print(' '.join(map(str, result)))
    #     print('\n')
