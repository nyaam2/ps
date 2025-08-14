n=int(input())
arr=[]
for i in range(n):
    a,c,b=map(int,input().split())
    arr.append((a,c,b))

# print(arr)

left=1
right=2147483647

while left<=right:
    mid=left+(right-left)//2
    cnt=0
    #print(f"left : {left}, right : {right}, mid : {mid}")
    for i in range(n):
        a,c,b=arr[i]
        if mid<a:
            continue
        if c>=mid:
            cnt+=(mid-a)//b+1
        else:
            cnt+=(c-a)//b+1
    if cnt%2==0:
        left=mid+1
    else:
        right=mid-1



num=left
cnt=0
for a,c,b in arr:
    if num<a:
        continue
    if c>=num:
        cnt+=(num-a)//b+1
    else:
        cnt+=(c-a)//b+1
    
if cnt%2==0:
    print("NOTHING")
else:
    dap=sum(1 for a,c,b in arr if a<=num<=c and (num-a)%b==0)
    print(num,dap)
    
