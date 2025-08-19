n,m=map(int,input().split())
board=[[0 for _ in range(m)] for _ in range(n)]
# print(board.shape)
for i in range(n):
    board[i]=list(map(int,input().split()))

from collections import deque


dx=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]

dq=deque()
def bfs(x,y):
    
    visited=[[False for _ in range(m)] for _ in range(n)]
    dq.append((x,y,0))
    visited[y][x]=True
    
    while dq:
        a,b,c=dq.popleft()
        visited[b][a]=True
        for i,j in dx:
                ny,nx=b+i,a+j
                if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                    
                    if board[ny][nx]==1:
                        return c+1
                    else:
                        dq.append((nx,ny,c+1))
    return 0
result=0
for i in range(n):
    for j in range(m):
        # print(i,j)
        if board[i][j]==1:
            continue
        result=max(result,bfs(j,i))
        # print(result)
        dq.clear()
print(result)


                    

