#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj, adj_r):
    result = 0
    #write your code here
    visited = [0]*len(adj)
    postorder_r, postorder = [], []
    def dfs(x, adj_, postorder):
        nonlocal visited
        
        visited[x] = 1
        for y in adj_[x]:
            if not visited[y]:
                dfs(y, adj_, postorder)
        
        postorder.append(x)
    
    # find the SINK = Source of reversed Graph
    for i in range(len(adj_r)):
        if not visited[i]:
            dfs(i, adj_r, postorder_r)

    visited = [0]*len(adj)
    for i in reversed(postorder_r):
        if not visited[i]:
            dfs(i, adj, postorder)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4,4,
    #        1,2,
    #        4,1,
    #        2,3,
    #        3,1]
    #2

    #data = [5,7,
    #        2,1,
    #        3,2,
    #        3,1,
    #        4,3,
    #        4,1,
    #        5,2,
    #        5,3]
    #5

    #data = [4, 3,
    #        1, 2,
    #        3, 2,
    #        4, 3]
    #4
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_r[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_r))


