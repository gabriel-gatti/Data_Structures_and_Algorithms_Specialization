#Uses python3

import sys
#from math import log

def negative_cycle(adj, cost):
    #write your code here
    def bellman_ford() -> bool:
        nonlocal dist, prev
        relaxation = 0
        for node in range(v-1):
            for i in range(len(adj[node])):
                viz, wei = adj[node][i], cost[node][i]

                #print('node:', node, 'viz', viz, 'dist_viz', dist[viz], 'dist_new',  dist[node] + wei)
                if dist[viz] > dist[node] + wei:
                    dist[viz] = dist[node] + wei
                    prev[viz] = node
                    relaxation = 1
                    #print("PREV:", prev, "DIST:", dist)
        
        return relaxation

    v = len(adj)
    dist, prev = [10000001]*v, [None]*v
    dist[0] = 0
    for _ in range(v):
        if not bellman_ford():
            break

    return bellman_ford()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))


    #data = [4,4,
    #        1,2,-5,
    #        4,1,2,
    #        2,3,2,
    #        3,1,1]
    # 1

    #data = [10, 10,
    #        1, 2, -1,
    #        5, 6, -1,
    #        6, 7, -1,
    #        8, 9, -1,
    #        9, 10,-1,
    #        7, 8, -1,
    #        4, 5, -1,
    #        2, 3, -1,
    #        3, 4, -1, 
    #        
    #        3, 5, -3]
    #0
#

    n, m = data[0:2]

    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
