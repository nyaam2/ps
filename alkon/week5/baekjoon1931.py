n=int(input())
arr=[]
for i in range(n):
    s,e=map(int,input().split())
    arr.append((s,e))

arr.sort(key=lambda x:(x[1],x[0]))

cnt=1
prev=arr[0][1]
for i in range(1,n,1):
    if prev<=arr[i][0]:
        cnt+=1
        prev=arr[i][1]
    else:
        continue

print(cnt)
    