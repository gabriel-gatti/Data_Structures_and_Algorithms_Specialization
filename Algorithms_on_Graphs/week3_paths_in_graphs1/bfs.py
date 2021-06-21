#Uses python3

import sys

def distance(adj, s, t):
    #write your code here
    dist = [float('inf')]*len(adj)
    dist[s], q = 0, [s]

    while q:
        node = q.pop(0)
        for i in adj[node]:    
            if dist[i] == float('inf'):
                q.append(i)
                dist[i] = dist[node] + 1
                if i == t:
                    return dist[t]

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4,4,
    #        1,2,
    #        4,1,
    #        2,3,
    #        3,1,
    #        2,4]
    # 2

    #data = [5,4,
    #        5,2,
    #        1,3,
    #        3,4,
    #        1,4,
    #        3,5]
    # -1
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
