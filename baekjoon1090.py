


n=int(input())
list=[]
for i in range(n):
    x,y=map(int,input().split())
    list.append((x,y))
dap=[100000000]*n
for i in range(n):
    for j in range(n):
        x=list[i][0]
        y=list[j][1]
        tmp=[]
        for k in range(n):
            a=abs(x-list[k][0])
            b=abs(y-list[k][1])
            tmp.append(a+b)

        tmp.sort()
        sum=0
        for k in range(n):
            sum+=tmp[k]
            if sum<dap[k]:
                dap[k]=sum
        

print(*dap[:])

    
