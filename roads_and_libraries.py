import sys


def cluster(row_start, m, c_name, clusters, visited):
    rows_queue = [row_start]
    for row in rows_queue:
        for col in m[row]:
            if col not in visited:
                c_name = min(c_name, m[row][col])
                if c_name not in clusters:
                    clusters[c_name] = 0
                if m[row][col] != c_name:
                    m[row][col] = c_name
                    if row != col:
                        clusters[c_name] += 1
                    for r in m:
                        if row in m[r]:
                            m[r][row] = c_name
                        if col in m[r]:
                            m[r][col] = c_name
                visited.add(row)
                if col > row:
                    rows_queue.append(col)


q = int(input().strip())
for a0 in range(q):
    clusters = {}
    n, m, x, y = input().strip().split(' ')
    n, m, lib_cost, road_cost = [int(n), int(m), int(x), int(y)]
    graph = {}
    # for i in range(n):
    #     graph.append({i: i + 1})  # (node_id, cluster id)
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1) - 1, int(city_2) - 1]
        if city_1 not in graph:
            graph[city_1] = {city_1: city_1 + 1}
        graph[city_1][city_2] = city_1 + 1

        if city_2 not in graph:
            graph[city_2] = {city_2: city_2 + 1}
        graph[city_2][city_1] = city_1 + 1
    print(graph)

    visited = set()
    for city in graph:
        cluster(city, graph, -(city + 1), clusters, visited)
    # print(matrix)
    print(clusters)
    print(graph)

    cost = 0
    if lib_cost >= road_cost:
        cost = len(clusters) * lib_cost
        for cluster_id in clusters:
            cost += clusters[cluster_id] * road_cost
    else:
        cost = n * lib_cost
    print(cost)
