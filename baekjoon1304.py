n,m=map(int,input().split())
graph = [0 for i in range(0,n+1,1)]


for i in range(m):
    s,e=map(int,input().split())
    if s<e: continue

    for j in range(e,s,1):
        graph[j]=1

for i in range(1,n+1,1):
    if n%i!=0:
        continue
    flag=False
    for j in range(i,n+1,i):
        if graph[j]==1:
            flag=True
            break
        else:
            flag=False
 
    if not flag:
        print(n//i)
        break
    else:
        continue

    
