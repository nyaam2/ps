c,n=map(int,input().split())
chicken=list(int(input()) for _ in range(c))

cow=[tuple(map(int,input().split())) for _ in range(n)]

print(chicken)
print(cow)


chicken.sort()
print(chicken)

import heapq
pq=[]
for i in cow:
    heapq.heappush(pq,(i[1],i[0]))
idx=0
dap=0
a=heapq.heappop(pq)
while pq and idx<len(chicken):

    if chicken[idx]<=a[0] and chicken[idx]>=a[1]:
        
        dap+=1
        idx+=1
        if pq:
            a=heapq.heappop(pq)
        else:
            break
    elif chicken[idx]<a[1]:
        idx+=1
    elif chicken[idx]>a[0]:
        if pq:
            a=heapq.heappop(pq)
        # else:
        #     break

        

print(dap)