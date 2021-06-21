#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    used[x] = 1
    for y in adj[x]:
        if not used[y]:
            dfs(adj, used, order, y)
        
    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    for i in range(len(adj)):
        if not used[i]:
            dfs(adj, used, order, i)
    

    return list(reversed(order))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4,3,
    #        1,2,
    #        4,1,
    #        3,1]
    # 4 3 1 2

    #data = [4,1,
    #        3,1]
    # 2 3 1 4

    #data = [5,7,
    #        2,1,
    #        3,2,
    #        3,1,
    #        4,3,
    #        4,1,
    #        5,2,
    #        5,3]
    # 5 4 3 2 1 

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

