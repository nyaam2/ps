n=int(input())
result=[]
for i in range(n):
    x,y,z=map(int,input().split())
    result.append((x,y,z))
result2=[]
#v=[[] for _ in range(10000)]
min1=100000000
for i in range(1,len(result),1):
    min2=100000000
    min3=100000000
    for j in range(0,len(result),1):
        if j==i:continue
        A=abs(result[i][0]-result[j][0])
        B=abs(result[i][1]-result[j][1])
        C=abs(result[i][2]-result[j][2])
        
        if A+B+C<min2:
            min3=min2
            min2=A+B+C
        elif A+B+C<min3:
            min3=A+B+C
       

    min1=min(min1,min2+min3)


print(min1)