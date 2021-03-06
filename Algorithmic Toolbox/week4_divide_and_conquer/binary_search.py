# Uses python3
import sys
"""
Binary Search:

Problem Introduction:
    In this problem, you will implement the binary search algorithm that allows searching
    very efficiently (even huge) lists, provided that the list is sorted.

Problem Description:
    Task: The goal in this code problem is to implement the binary search algorithm.
    
    Input Format: The first line of the input contains an integer ๐ and a sequence ๐ 0 < ๐ 1 < . . . < ๐ ๐โ1
        of ๐ pairwise distinct positive integers in increasing order. The next line contains an integer ๐ and ๐
        positive integers ๐ 0 , ๐ 1 , . . . , ๐ ๐โ1 .
    
    Constraints: 1 โค ๐ โค 10 5 ; 1 โค ๐ โค 3 ยท 10 4 ; 1 โค ๐ ๐ โค 10 9 for all 0 โค ๐ < ๐; 1 โค ๐ ๐ โค 10 9 for all 0 โค ๐ < ๐;
    
    Output Format: For all ๐ from 0 to ๐ โ 1, output an index 0 โค ๐ โค ๐ โ 1 such that ๐ ๐ = ๐ ๐ or โ1 if there
        is no such index.
    
Sample:
    Input:
        5 1 5 8 12 13
        5 8 1 23 1 11
    Output:
        2 0 -1 0 -1

    In this sample, we are given an increasing sequence ๐ 0 = 1, ๐ 1 = 5, ๐ 2 = 8, ๐ 3 = 12, ๐ 4 = 13 of length
    five and five keys to search: 8, 1, 23, 1, 11. We see that ๐ 2 = 8 and ๐ 0 = 1, but the keys 23 and 11 do
    not appear in the sequence ๐. For this reason, we output a sequence 2, 0, โ1, 0, โ1.
"""
def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    def rec(l, r):
        mid = (r - l)//2 + l
        if a[mid] == x:
            return mid
        if mid == len(a)-1 or mid == 0:
            return -1
        elif a[mid] > x:
            return rec(l, mid-1)
        else:
            return rec(mid+1, r)

    return rec(left, right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

