from collections import deque
n=int(input())
arr=[]
m=dict()
cnt=0
for i in range(n):
    num=int(input())
    arr.append(num)
 

arr2=sorted(arr)

# print(arr)
# print(arr2)


for i in range(n):
    m[arr2[i]]=cnt
    cnt+=1
# print(m)
d=[ deque() for _ in range(50)]
idx=1
d[0].append(arr[0])
for i in range(1,n,1):
    flag=False
    for j in range(idx):
        if m[d[j][0]]-m[arr[i]]==1:
            flag=True
            d[j].appendleft(arr[i])
        elif m[d[j][-1]]-m[arr[i]]==-1:
            flag=True
            d[j].append(arr[i])
        if flag==True:
            break
    if flag==False:
        print(arr[i])
        d[idx].append(arr[i])
        idx+=1
print(idx)





    
        
