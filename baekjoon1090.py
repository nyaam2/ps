n=int(input())
list=[]

for i in range(n):
    x,y=map(int,input().split())
    list.append((x,y))

dap=[100000000 for _ in range(n)]
for i in range(n):
    x=list[i][0] 
    for j in range(n):
        y=list[j][1]
        distance=[]
        for k in range(0,n,1):
            distance.append(abs(x-list[k][0])+abs(y-list[k][1]))
        
        sum_=0
      
        for k in range(0,n,1):
         
            sum_+=distance[k]
            if dap[k]>sum_:
                dap[k]=sum_
            
print(*dap[:])