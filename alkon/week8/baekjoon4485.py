import sys
import heapq
input = sys.stdin.readline
idx=1
while True:

    n=int(input())
    if n==0:
        exit()
    board=[[]for _ in range(n)]
    for i in range(n):
        board[i]=list(map(int,input().split()))
    #print(board)
    INF=10**18
    dist=[ [INF for _ in range(n)]for _ in range(n)]
    #print(dist)

    dist[0][0]=board[0][0]

    dd=[(0,1),(1,0),(-1,0),(0,-1)]

    pq=[(board[0][0],0,0)]

    while pq:
        d,u1,u2=heapq.heappop(pq)

        if dist[u1][u2]<d:
            continue

        for dx,dy in dd:
            ddy=dy+u1; ddx=dx+u2
            if ddy>=0 and ddy<n and ddx>=0 and ddx<n:
                # if dist[ddy][ddx]==INF:
                    ddd=board[ddy][ddx]+d
                    if ddd<dist[ddy][ddx]:
                        dist[ddy][ddx]=ddd
                        heapq.heappush(pq,(ddd,ddy,ddx))

    print(f"Problem {idx}: {dist[n-1][n-1]}")
    idx+=1






