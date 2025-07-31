n=int(input())
arr=[]
for i in range(n):
    a,c,b=map(int,input().split())
    arr.append((a,c,b))

start=1
end=2_147_483_647

while start<=end:
    mid=start+(end-start)//2
    # print(f"start : {start}, end : {end}")
    cnt=0
    for i in arr:
        a,c,b=i
        if mid<a:
            continue
        minValue=min(c,mid)
        
        cnt+=(minValue-a)//b+1
    
    if cnt%2==0:
        start=mid+1
    else:
        end=mid-1


num=start
minValue=0
cnt=0
for i in arr:
    a,c,b=i
    if num<a or num>c:
        continue
    if (num-a)%b==0:
        cnt+=1

if cnt%2==0:
    print("NOTHING")
else:
    print(num,cnt)