m,n=map(int,input().split())


board=[[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board[i]=list(map(int,input().split()))
from collections import deque


dd=[(-1,0),(1,0),(0,-1),(0,1)]

dq=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            dq.append((j,i,0))
dap=0
while dq:
    a,b,c=dq.popleft()
    for dx,dy in dd:
        nx,ny=a+dx,b+dy
        if 0<=nx<m and 0<=ny<n and board[ny][nx]==0:
            board[ny][nx]=board[b][a]+1
            dq.append((nx,ny,c+1))
            dap=max(dap,c+1)

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(-1)
            exit()
print(dap)


    
            



