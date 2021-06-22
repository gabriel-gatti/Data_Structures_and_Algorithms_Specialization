#Uses python3
import sys
from itertools import combinations

def minimum_distance(x, y):
    result = 0
    #write your code here
    def find(key):
        for i, set in enumerate(sets):
            if key in set:
                return i

    k = len(x)
    sets = [set([i]) for i in range(k)]
    combs = combinations(range(k), 2)
    edges = sorted([(i, j, ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5) for i, j in combs ], key=lambda e: e[2])
    for i, j, d in edges:
        ii, ij = find(i), find(j)
        #print(sets)
        if ii != None and ij != None and ii != ij:
            #print((i,j,d), (ii, sets[ii]), (ij, sets[ij]))
            sets[ii] = sets[ii].union(sets[ij])
            sets.pop(ij)
            result += d
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [4,
    #        0,0,
    #        0,1,
    #        1,0,
    #        1,1]
    # 3

    #data = [5,
    #        0,0,
    #        0,2,
    #        1,1,
    #        3,0,
    #        3,2]
    # 7.064495102

    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
