d,num=map(str,input().split())

x,y=map(int,input().split())

a,b=0,0
t=int(d)-1
for i in num:
    
    if i=='1':
        a+=pow(2,t)
    if i=='2':
        continue
    if i=='3':
        b+=pow(2,t)
    if i=='4':
        a+=pow(2,t)
        b+=pow(2,t)
    t-=1
# print(a,b)

a+=x
b-=y

limit=pow(2,int(d))
if not (0<=a<limit and 0<=b<limit):
    print(-1)
    exit()
tt=int(d)-1
dap=""
def go():
    global a,b,tt,dap

    if tt==-1:
        return
    p=pow(2,tt)

    #4사분면
    if p<=a and p<=b:
        a-=p
        b-=p
        dap+="4"
    #1사분면
    elif p<=a and b<p:
        a-=p
        dap+="1"
    #3사분면
    elif a<p and p<=b :
        b-=p
        dap+="3"
    elif 0<=a<p and 0<=b<p:
        dap+="2"
    else:
        print(-1)
        exit()

    tt-=1
    go()

go()
print(dap)
        





