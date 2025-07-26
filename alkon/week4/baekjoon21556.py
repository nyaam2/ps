from itertools import combinations
from math import comb
import math
n=int(input())
arr=list(map(int,input().split()))
arr2=[]
for co in combinations(arr,2):
    arr2.append(co[0]+co[1])

arr2.sort()
print(arr2)
print(arr2[math.ceil((len(arr2)-1)/2)])
