n,x,y,z=map(int,input().split())
maxValue=max(x,y,z)

left=1
right=maxValue*n
t=0
while left<=right:
    mid=left+(right-left)//2

    cnt=0
    cnt+=(mid//x)+(mid//y)+(mid//z)
    print(f"mid, left, right : {mid,left,right}")
    if cnt>=n:
        right=mid-1
    elif cnt<n:
        left=mid+1
    # else:
    #     if mid//z==0:
    #         print("C win")
    #     elif mid//y==0:
    #         print("B win")
    #     elif mid//x==0:
    #         print("C win")
        
    #     exit()

# print(t)
# print(mid)
print(left)
t=left
beforeBallon=(t-1)//x+(t-1)//y+(t-1)//z
# print(beforeBallon)
arr=[]
arr.append(x)
arr.append(y)
arr.append(z)

for i in range(3):
    if t%arr[i]==0:
        beforeBallon+=1
        if beforeBallon==n:
            if i==0:
                print("A win")
            elif i==1:
                print("B win")
            elif i==2:
                print("C win")
            exit()

