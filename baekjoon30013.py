n=int(input())
s=input()
l=list(s)

dap=100000000


for i in range(1,n+1,1):
    cnt=0
    visited=[False]*n
    for j in range(0,n,1):
        k=j
        flag=False
        while k<n and visited[k]!=True and l[k]=='#':
            visited[k]=True
            k+=i
            flag=True
        if flag:
            cnt+=1
    if cnt!=0:
        dap=min(dap,cnt)
if dap==100000000:
    print(0)
else:
    print(dap)
    

    

