# Uses python3
import sys
"""
Binary Search:

Problem Introduction:
    In this problem, you will implement the binary search algorithm that allows searching
    very efficiently (even huge) lists, provided that the list is sorted.

Problem Description:
    Task: The goal in this code problem is to implement the binary search algorithm.
    
    Input Format: The first line of the input contains an integer 𝑛 and a sequence 𝑎 0 < 𝑎 1 < . . . < 𝑎 𝑛−1
        of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘
        positive integers 𝑏 0 , 𝑏 1 , . . . , 𝑏 𝑘−1 .
    
    Constraints: 1 ≤ 𝑘 ≤ 10 5 ; 1 ≤ 𝑛 ≤ 3 · 10 4 ; 1 ≤ 𝑎 𝑖 ≤ 10 9 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏 𝑗 ≤ 10 9 for all 0 ≤ 𝑗 < 𝑘;
    
    Output Format: For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎 𝑗 = 𝑏 𝑖 or −1 if there
        is no such index.
    
Sample:
    Input:
        5 1 5 8 12 13
        5 8 1 23 1 11
    Output:
        2 0 -1 0 -1

    In this sample, we are given an increasing sequence 𝑎 0 = 1, 𝑎 1 = 5, 𝑎 2 = 8, 𝑎 3 = 12, 𝑎 4 = 13 of length
    five and five keys to search: 8, 1, 23, 1, 11. We see that 𝑎 2 = 8 and 𝑎 0 = 1, but the keys 23 and 11 do
    not appear in the sequence 𝑎. For this reason, we output a sequence 2, 0, −1, 0, −1.
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

