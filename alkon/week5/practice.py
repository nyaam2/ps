e,em,m,mh,h=map(int,input().split())
dap=0
while True:
    if e!=0 or em!=0:
        if e!=0:
            e-=1
        elif em!=0:
            em-=1
    else:
        break
    if m!=0 or em!=0 or mh!=0:
        if m!=0:
            m-=1
        # else:
        #     if em>=mh:
        #         em-=1
        #     else:
        #         mh-=1
        else:
            if em>mh:
                em-=1
            else:
                mh-=1
    #만약 이렇게 하면, 0 2 0 2 0인 상황에서 반례나옴
    
    else:
        break
    if h!=0 or mh!=0:
        if h!=0:
            h-=1
        elif mh!=0:
            mh-=1
    else:
        break
    dap+=1
print(dap)