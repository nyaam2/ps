n=int(input())

list=[]
dap=100000000
for i in range(n):
    x,y,z=map(int,input().split())
    list.append((x,y,z))
for i in range(1,n,1):
    min1=100000000
    min2=100000000
    for j in range(0,n,1):
        if i==j:
            continue
        a=abs(list[i][0]-list[j][0])
        b=abs(list[i][1]-list[j][1])
        c=abs(list[i][2]-list[j][2])

        if min1>a+b+c:
            min2=min1
            min1=a+b+c
        elif min2>a+b+c:
            min2=a+b+c
        dap=min(dap,min1+min2)

print(dap)
        
