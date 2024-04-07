#!/usr/bin/python
from itertools import combinations
def binomial(n,k):
    L=[]
    for i in range(0,n):
        L.append(i)
    combinaciones=list(combinations(L,k))
    return len(combinaciones)

binomial(6,4)
