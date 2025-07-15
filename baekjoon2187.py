n,a,b=map(int,input().split())

maxA=2000000
maxB=2000000

list=[]
for i in range(n):
    r,c,s=map(int,input().split())
    list.append((r,c,s))


dap=0
for i in range(len(list)):
    for j in range(i+1,len(list),1):
        if (abs(list[i][0]-list[j][0])<a)and(abs(list[i][1]-list[j][1])<b):
            dap=max(dap,abs(list[i][2]-list[j][2]))
print(dap)

