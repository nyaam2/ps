n=int(input())
list=input()
dap=100000000
for i in range(1,2001,1):
    visited=[0]*2001
    tmpDap=0
    for j in range(0,n,1):
        if visited[j]==0 and list[j]=='#':
           
            while j<n and list[j]=='#':
                visited[j]=1
                j+=i
                
            tmpDap+=1
        else:
            continue
    if tmpDap!=0:
        dap=min(dap,tmpDap)
if dap==100000000:
    print(0)
else:
    print(dap)


