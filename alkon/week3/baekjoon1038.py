from collections import deque


n=int(input())

d=deque()
idx=-1
for i in range(10):
    d.append(str(i))
    idx+=1
if n<idx:
    print(n)
    exit()

while idx<n and len(d)!=0:
    b=int(d.popleft())

    a=b%10
    for i in range(10):
        if idx<n:
            if i<a:
                d.append(str(b)+str(i))
                idx+=1
if len(d)!=0:
    print(d[-1])
else:
    print(-1)
            
