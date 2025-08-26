import sys
input = sys.stdin.readline
n,m=map(int,input().split())
g=[]
for i in range(m):
    s,e,c=map(int,input().split())
    g.append((s,e,c))

# print(g)

g.sort(key=lambda x: x[2])

# print(g)

parent=[0 for _ in range(n+1)]
for i in range(1,n+1,1):
    parent[i]=i

def find(a):
    global g
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
def isCycle(a,b):
    if find(a)==find(b):
        return True
    else:
        return False
dap=0
visited=[False for _ in range(n+1)]
for i in range(m):
    s,e,c=g[i]
    if c>=n+1:
        continue
    if isCycle(s,e):
        continue
    union(s,e)
    dap=max(dap,c)
    visited[c]=True
for i in range(1,n+1,1):
    if visited[i]==False:
        print(i)
        exit()


print(dap+1)

    


    



    