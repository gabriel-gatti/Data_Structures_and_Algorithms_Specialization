#Uses python3

import sys

def dfs(visited, x, adj):
    if visited[x][0]:
        if not visited[x][1]:
            return 1
    else:
        visited[x][0] = True
        for i in adj[x]:
            if dfs(visited, i, adj):
                return 1
        visited[x][1] = True
    return 0

def acyclic(visited, n, adj):
    for i in range(n):
        if not visited[i][0]:
            visited[i][0] = True
            for a in adj[i]:
                if dfs(visited, a, adj):
                    return 1
            visited[i][1] = True
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4, 4,
    #        1, 2,
    #        4, 1,
    #        2, 3,
    #        3, 1]
    #1
#
    #data = [5, 7,
    #        1, 2,
    #        2, 3,
    #        1, 3,
    #        3, 4,
    #        1, 4,
    #        2, 5,
    #        3, 5]
    ### 0
    #
    #data = [4, 3,
    #        1, 2,
    #        3, 2,
    #        4, 3]
    #0

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [[False, False] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(visited, n, adj))