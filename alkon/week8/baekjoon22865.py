import heapq
n=int(input())
a,b,c=map(int,input().split())
m=int(input())
g=[[]for _ in range(n+1)]
for i in range(m):
    s,e,cc=map(int,input().split())
    g[s].append((e,cc))
    g[e].append((s,cc))

# print(g)
INF=10**18

def dijkstra(start):
    global g
    global n
    dist=[INF]*(n+1)
    dist[start]=0
    pq=[(0,start)]

    while pq:
        d,u=heapq.heappop(pq)

        if dist[u]<d:
            continue
        
        for v,w in g[u]:
            dd=d+w

            if dd<dist[v]:
                dist[v]=dd
                heapq.heappush(pq,(dd,v))

    return dist
result1=0
result2=INF
d1=dijkstra(a)
d2=dijkstra(b)
d3=dijkstra(c)

for i in range(1,n+1,1):
    if i==a or i==b or i==c:
        continue
    v = min(d1[i], d2[i], d3[i])
    if v>=INF:
        continue
    if result1<=v:
        if result1==v:
            result1=min(d1[i],d2[i],d3[i])
            result2=min(result2,i)
        else:
            result1=min(d1[i],d2[i],d3[i])
            result2=i

       
        

print(result2)






