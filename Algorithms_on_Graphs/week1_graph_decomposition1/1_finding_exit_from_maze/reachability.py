#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    visited = [False]*len(adj)
    result = []
    def rec(x:int, y:int) -> None:
      visited[x] = True

      if x==y:
        result.append(1)
        return

      for i in adj[x]:
        if not visited[i]:
          rec(i,y)
      return

    rec(x, y)
    return sum(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
