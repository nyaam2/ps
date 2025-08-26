
#정렬로 접근하려고 했음.
# n=int(input())
# m=int(input())
# g=[]
# for _ in range(m):
#     s,e,c=map(int,input().split())
#     g.append((s,e,c))

# g.sort(key=lambda x: x[2])  # 가중치 기준으로 정렬
# print(g)
# start,end=map(int,input().split())
# dap=0
# res=[[]for _ in range(n+1)]
# dist=[100000000 for _ in range(n+1)]

# for i in range(m):
    
#     s,e,c=g[i]
   
#     if dist[s]<c:
#         continue
   
#     res[s].append((e,c))
    
#     if dist[e]<c:
#         continue
#     if e==end:
#         break
#     dist[e]=c

# dap=0
# print(dist[end])


#데이크스트라
import heapq
import sys
input = sys.stdin.readline
INF=10**18

n=int(input())
m=int(input())
g=[[]for _ in range(n+1)]
for _ in range(m):
    s,e,c=map(int,input().split())
    g[s].append((e,c))
start,end=map(int,input().split())

def dijkstra(n,g,start):
    dist=[INF]*(n+1)
    dist[start]=0

    pq=[(0,start)]

    while pq:
        d,u=heapq.heappop(pq)

        if d!=dist[u]:
            continue
        
        for v,w in g[u]:
            nd=d+w

            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(pq,(nd,v))
    return dist

dist=dijkstra(n,g,start)
# print(dist)
print(dist[end])
    

    






