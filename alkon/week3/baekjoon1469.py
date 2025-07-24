n=int(input())
arr=list(map(int,input().split()))

arr2=[-1 for _ in range(2*n)]
visited=[False for _ in range(17)]
arr.sort()
def go(idx):
    global arr
    global arr2
    if idx==2*n:
        print(*arr2)
        exit()
    if arr2[idx]!=-1:
        go(idx+1)
        return
    for i in arr:
        if visited[i]==True:
            continue       
      
        if idx+i+1<2*n: 
            if arr2[idx+i+1]!=-1:
                continue
            arr2[idx+i+1]=i
            arr2[idx]=i
        else:
            continue
        visited[i]=True
        go(idx+1)
        visited[i]=False
        arr2[idx+i+1]=-1
        arr2[idx]=-1

go(0)
print(-1)
