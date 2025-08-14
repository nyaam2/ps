d,num=input().split()
x,y=map(int,input().split())
list=list(num)

n=int(d)
n=2**n
r,c=0,0 #row, column


for i in num:
    n=n//2
    if i=='1':
        c+=n
    elif i=='2':
        continue
    elif i=='3':
        r+=n
    else:
        r+=n
        c+=n
# print(r,c)

r-=y
c+=x

n=2**int(d)
ans=''

while n>1:
    if 0<=r<n//2 and 0<=c<n//2:
        ans+='2'

    elif 0<=r<n//2 and n//2<=c<n:
        c-=n//2
        ans+='1'
    elif n//2<=r<n and 0<=c<n//2:
        r-=n//2
        ans+='3'
    elif n//2<=r<n and n//2<=c<n:
        r-=n//2
        c-=n//2
        ans+='4'
    else:
        print(-1)
        exit()
    n=n//2

print(ans)





