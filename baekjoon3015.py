n=int(input())
s=[]
dap=0
for i in range(n):
    x=int(input())
    cnt=1
 
    while len(s)!=0 and s[-1][0]<=x:
        if x==s[-1][0]:
             cnt+=s[-1][1]
        dap+=s[-1][1]
        s.pop()
    if len(s)!=0:
        dap+=1
    s.append((x,cnt))
print(dap)

