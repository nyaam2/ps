import heapq

n,m=map(int,input().split())
arr=list(map(int,input().split()))
pq=[]
sum=0
dap=0
for i in range(n):
    heapq.heappush(pq,-arr[i])
    sum+=arr[i]

   
    if sum>=m:
        out=-heapq.heappop(pq)*2
        sum-=out
     
        dap+=1
print(dap)
