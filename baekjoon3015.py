n=int(input())
s=[]
dap=0
for i in range(n):
    a=int(input())
    cnt=1
    while len(s)!=0 and s[-1][0]<=a:
        if s[-1][0]==a:
            cnt+=s[-1][1]
             
        dap+=s[-1][1]
        s.pop()
    
    if len(s)!=0:
        dap+=1
    s.append((a,cnt))
print(dap)


    