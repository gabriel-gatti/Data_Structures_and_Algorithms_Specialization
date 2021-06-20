#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    visited = [False]*len(adj)

    def dfs(x):
        visited[x] = True
        for y in adj[x]:
            if not visited[y]:
                dfs(y)
    
    result = 0
    for i in range(len(adj)):
        if not visited[i]:
            dfs(i)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
