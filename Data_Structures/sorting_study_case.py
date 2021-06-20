# Uses python3
import sys
import random

def insert_sort(a):
    if len(a)==1:
        return a

    for i in range(1, len(a)):
        k = a[i]
        for j in reversed(range(0, i)):
            if a[j] <= k:
                j = j+1
                break
            a[j+1] = a[j]
            
        a[j] = k

    return a


def merge_sort(a, l, r):
    def merge(l_, m_, r_):
        L = a[l_:m_]
        R = a[m_:r_]

        i = 0 #L Counter
        j = 0 #R Counter
        for k in range(l_, r_):
            if j == len(R):
                a[k] = L[i]
                i+=1
            elif i == len(L):
                a[k] = R[j]
                j+=1
            elif L[i] < R[j]:
                a[k] = L[i]
                i+=1
            else:
                a[k] = R[j]
                j+=1

    if r-l>1:
        m = (r-l)//2+l
        merge_sort(a, l, m)
        merge_sort(a, m, r)
        merge(l, m, r)

    return a



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    def partition2(a, l, r):
        x = a[l]
        j = l
        for i in range(l + 1, r + 1):
            if a[i] <= x:
                j += 1
                a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], a[l]
        return j

    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

    return a

def trhee_way_randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    def partition3(a, l, r):
        #write your code here
        x=a[l]
        j=l
        for i in range(l+1, r+1):
            if a[l]<x:
                j+=1
                a[i], a[j] = a[j], a[i]
            elif a[l]==x:
                j+=1
        a[l], a[j] = a[j], a[l]
        return j

    m = partition3(a, l, r)
    trhee_way_randomized_quick_sort(a, l, m - 1);
    trhee_way_randomized_quick_sort(a, m + 1, r);
    return a

def counting_sort(a):
    min_ = min(a)
    max_ = max(a)

    c=[0]*(max_-min_+1) #O(n)
    b=[None]*len(a)
    for i in range(len(a)):
        c[a[i]-min_] += 1

    for j in range(min_+1, max_+1):
        c[j-min_] += c[j-min_-1]
    
    for i in reversed(range(len(a))):
        b[c[a[i]-min_]-1] = a[i]
        c[a[i]-min_] -= 1

    return b

A = [2,5,3,0,2,3,0,3]

print(counting_sort(A))
