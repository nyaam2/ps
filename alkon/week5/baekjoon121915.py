e,em,m,mh,h=map(int,input().split())
dap=0
while True:
    if e>0 or em>0:
        if e>0:
            e-=1
        elif em>0:
            em-=1
    else:
        break
    if m>0 or em>0 or mh>0:
        if m>0:
            m-=1
        elif em>0 or mh>0:
            if em>mh:
                em-=1
            elif em<mh:
                mh-=1
            else:
                em-=1
    else:
        break
    if h>0 or mh>0:
        if h>0:
            h-=1
        elif mh>0:
            mh-=1
    else:
        break
    dap+=1

print(dap)