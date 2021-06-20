# Uses python3
import sys
'''
Majority Element

Problem Introduction:
    Majority rule is a decision rule that selects the alternative which has a majority,
    that is, more than half the votes.
    Given a sequence of elements 𝑎 1 , 𝑎 2 , . . . , 𝑎 𝑛 , you would like to check whether
    it contains an element that appears more than 𝑛/2 times. A naive way to do
    this is the following.

Problem Description:
    Task: The goal in this code problem is to check whether an input sequence contains a majority element.
    Input Format: The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
        integers 𝑎 0 , 𝑎 1 , . . . , 𝑎 𝑛−1 .
    Constraints: 1 ≤ 𝑛 ≤ 10 5 ; 0 ≤ 𝑎 𝑖 ≤ 10 9 for all 0 ≤ 𝑖 < 𝑛.
    Output Format: Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
        and 0 otherwise.

Sample 1:
    Input:
        5
        23922
    Output:
        1
        2 is the majority element.
Sample 2:
    Input:
        4
        1234
    Output:
        0
        There is no majority element in this sequence.

What To Do:
    As you might have already guessed, this problem can be solved by the divide-and-conquer algorithm in time
    𝑂(𝑛 log 𝑛). Indeed, if a sequence of length 𝑛 contains a majority element, then the same element is also
    a majority element for one of its halves. Thus, to solve this problem you first split a given sequence into
    halves and make two recursive calls. Do you see how to combine the results of two recursive calls?
    It is interesting to note that this problem can also be solved in 𝑂(𝑛) time by a more advanced (non-divide
    and conquer) algorithm that just scans the given sequence twice.
'''

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 2 == right:
        return a[left]
    #write your code here
    mid = (right - left)// 2 + left
    maj_l = get_majority_element(a, left, mid)
    maj_r = get_majority_element(a, mid+1, right)
    return maj_l if maj_l == maj_r else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
