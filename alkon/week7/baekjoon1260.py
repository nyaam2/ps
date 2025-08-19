from collections import deque
n,m,v=map(int,input().split())

g=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n+1):
    g[i].sort()

def dfs(start,visited):
    print(start,end=' ')
    visited[start]=True
    for i in g[start]:
        if not visited[i]:
            dfs(i,visited)
dq=deque()

def bfs(start,visited):
    dq.append(start)
    visited[start]=True
    while dq:
        a=dq.popleft()
        print(a,end=' ')
        for i in g[a]:
            if not visited[i]:
                visited[i]=True
                dq.append(i)



visited=[False for _ in range(n+1)]
(dfs(v,visited))
print()
visited=[False for _ in range(n+1)]
(bfs(v,visited))
