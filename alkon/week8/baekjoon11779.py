import sys
input = sys.stdin.readline
import heapq
path=[]
n=int(input())
m=int(input())

g=[[]for _ in range(n+1)]
for i in range(m):
    s,e,c=map(int,input().split())
    g[s].append((e,c))
INF=10**18
dist=[INF for _ in range(n+1)]

start,end=map(int,input().split())

pq=[(start,0)]

dist[start]=0

while pq:
    u,d=heapq.heappop(pq)

    if dist[u]<d:
        continue

    for v,w in g[u]:
        dd=w+d
        if dist[v]>dd:
            dist[v]=dd
            heapq.heappush(pq,(v,dd))

print(dist[end])
