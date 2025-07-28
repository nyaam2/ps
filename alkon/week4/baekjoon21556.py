from itertools import combinations
from math import comb
import math
n=int(input())
arr=list(map(int,input().split()))


arr.sort()
lo = arr[0] + arr[1]
hi = arr[-1] + arr[-2]
need = math.floor((n*(n-1)//2 - 1)/2)
# print(lo,hi,need)

ans=0
while lo<=hi:
    mid=lo+(hi-lo)//2
    cnt=0
    j=n-1
    for i in range(n):
        while j>i and arr[i]+arr[j]>mid:
            j-=1
        cnt+=max(0,j-i)
    if cnt>need:
        hi=mid-1
        
        ans=mid
    else:
       
        lo=mid+1

print(ans)
