n=int(input())
arr=[0 for _ in range(6)]
for i in range(1,n+1,1):
    arr[i]=int(input())
dp=[[[[[[[-1 for _ in range(11)] 
         for _ in range(11)]
            for _ in range(11)]
              for _ in range(11)]
                for _ in range(11)] 
                   for _ in range(8)]
                     for _ in range(8)] 
                    


def go(prev,pprev,a,b,c,d,e):
    if a==0 and b==0 and c==0 and d==0 and e==0:
        return 1
    res=dp[prev][pprev][a][b][c][d][e]
    if res!=-1:
        print(f"Returning cached result for {prev}, {pprev}, {a}, {b}, {c}, {d}, {e}: {res}")
        return res
    res=0
    if a>0 and prev!=1 and pprev!=1:
        res+=go(1,prev,a-1,b,c,d,e)
    if b>0 and prev!=2 and pprev!=2:
        res+=go(2,prev,a,b-1,c,d,e)
    if c>0 and prev!=3 and pprev!=3:
        res+=go(3,prev,a,b,c-1,d,e)
    if d>0 and prev!=4 and pprev!=4:
        res+=go(4,prev,a,b,c,d-1,e)
    if e>0 and prev!=5 and pprev!=5:
        res+=go(5,prev,a,b,c,d,e-1)
    dp[prev][pprev][a][b][c][d][e] = res  # 저장!

    return res

print(go(7, 6, arr[1], arr[2], arr[3], arr[4], arr[5]))


#
# 경로 P1: C → D → A → B

# C: go(3,7, 2,2,0,1,0)

# D: go(4,3, 2,2,0,0,0)

# A: go(1,4, 1,2,0,0,0)

# B: go(2,1, 1,1,0,0,0) ⟵ 상태 S

# 경로 P2: D → C → A → B

# D: go(4,7, 2,2,1,0,0)

# C: go(3,4, 2,2,0,0,0)

# A: go(1,3, 1,2,0,0,0)

# B: go(2,1, 1,1,0,0,0) ⟵ 똑같이 상태 S