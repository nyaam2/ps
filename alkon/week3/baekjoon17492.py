n=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)] 
cnt=0
for i in range(n):
    arr[i]=list(map(int,input().split()))
    for j in arr[i]:
       if j==2:
          cnt+=1

def go():
    global cnt
    if cnt==1:
       print("Possible")
       exit()
    # for i in arr:
    #     print(i,end="\n")

    print()
    for x in range(n):
       for y in range(n):
            if arr[x][y]!=2:
                continue
            if x+1<n-1 and arr[x+1][y]==2 and x+2<n-1 and arr[x+2][y]==0:
                arr[x][y]=0
                arr[x+1][y]=0
                arr[x+2][y]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x+1][y]=2
                arr[x+2][y]=0
                cnt+=1
            if y+1<n-1 and arr[x][y+1]==2 and y+2<n-1 and arr[x][y+2]==0:
                arr[x][y]=0
                arr[x][y+1]=0
                arr[x][y+2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x][y+1]=2
                arr[x][y+2]=0
                cnt+=1
            if 0<x-1 and arr[x-1][y]==2 and 0<x-2 and arr[x-2][y]==0:
                arr[x][y]=0
                arr[x-1][y]=0
                arr[x-2][y]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x-1][y]=2
                arr[x-2][y]=0
                cnt+=1
            if 0<y-1 and arr[x][y-1]==2 and 0<y-2 and arr[x][y-2]==0:
                arr[x][y]=0
                arr[x][y-1]=0
                arr[x][y-2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x][y-1]=2
                arr[x][y-2]=0
                cnt+=1
            if 0<x-1 and y+1<n-1 and arr[x-1][y+1]==2 and 0<x-2 and y+2<n-1 and arr[x-2][y+2]==0:
                arr[x][y]=0
                arr[x-1][y+1]=0
                arr[x-2][y+2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x-1][y+1]=2
                arr[x-2][y+2]=0
                cnt+=1
            if x+1<n-1 and y+1<n-1 and arr[x+1][y+1]==2 and x+2<n-1 and y+2<n-1 and arr[x+2][y+2]==0:
                arr[x][y]=0
                arr[x+1][y+1]=0
                arr[x+2][y+2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x+1][y+1]=2
                arr[x+2][y+2]=0
                cnt+=1
            if 0<x-1 and 0<y+1 and arr[x-1][y-1]==2 and 0<x-2 and 0<y-2 and arr[x-2][y-2]==0:
                arr[x][y]=0
                arr[x-1][y-1]=0
                arr[x-2][y-2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x-1][y-1]=2
                arr[x-2][y-2]=0
                cnt+=1
            if x+1<n-1 and 0<y-1 and arr[x+1][y+1]==2 and x+2<n-1 and 0<y-2 and arr[x+2][y-2]==0:
                arr[x][y]=0
                arr[x+1][y-1]=0
                arr[x+2][y-2]=2
                cnt-=1
                go() 
                arr[x][y]=2
                arr[x+1][y-1]=2
                arr[x+2][y-2]=0
                cnt+=1
                
go()

print("Impossible")
    

