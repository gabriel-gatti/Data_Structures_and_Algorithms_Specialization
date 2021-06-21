#Uses python3

import sys
#import queue

def bipartite(adj):
    #write your code here
    dist = [float('inf')]*len(adj)
    q = []
    
    for i, v in enumerate(adj):
        if len(v) and dist[i] == float('inf'):
            dist[i], s, q = 1, i, [i]
            
            while q:
                node = q.pop(0)

                for j in adj[node]:
                    if dist[j] == float('inf'):
                        dist[j] = -dist[node]
                        q.append(j)

                    elif dist[j] == dist[node]:
                        return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4,4,
    #        1,2,
    #        4,1,
    #        2,3,
    #        3,1]
    # 0

    #data = [5,4,
    #        5,2,
    #        4,2,
    #        3,4,
    #        1,4]
    # 1
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
