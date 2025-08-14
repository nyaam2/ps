n=int(input())
m=dict()
arr=[]
visited=[False for _ in range (500000)]
for i in range(n):
    num=int(input())
    arr.append(num)
    m[num]=num


for i in range(0,n,1):
    if visited[arr[i]]==True:
        continue
    for j in range(max(1,arr[i]-1),min(n,arr[i]+1)+1,1):
        if visited[j]==True:
            continue
        
        m[arr[i]]=j
        m[j]=arr[i]
        visited[j]=True
        visited[arr[i]]=True
        break
    
# print("\n"*3) # For Test

for value in m:
    print(m[value])
