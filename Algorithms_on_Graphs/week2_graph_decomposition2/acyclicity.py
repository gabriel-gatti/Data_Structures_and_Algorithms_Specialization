#Uses python3

import sys


def acyclic(adj):
    # 0 Unvisited
    # 1 Currently Visiting
    #-1 Already Visited
    visited = [0]*len(adj)
    result = 0
    def dfs(x):
        nonlocal result
        nonlocal visited

        visited[x] = 1
        for y in adj[x]:
            if visited[y] == 1:
                result = 1

            elif visited[y] == 0:
                dfs(y)
                visited = [(0 if k==0 else -1) for k in visited]

    for i in range(len(adj)):
        if visited[i] == 0:
            dfs(i)
            visited = [(0 if k==0 else -1) for k in visited]

    return result 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4, 4,
    #        1, 2,
    #        4, 1,
    #        2, 3,
    #        3, 1]

    #1
    #data = [5, 7,
    #        1, 2,
    #        2, 3,
    #        1, 3,
    #        3, 4,
    #        1, 4,
    #        2, 5,
    #        3, 5]
    # 0
    #data = [4, 3,
    #        1, 2,
    #        3, 2,
    #        4, 3]

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
