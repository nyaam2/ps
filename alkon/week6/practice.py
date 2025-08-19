n=int(input())
arr=[0 for _ in range(5)]
for i in range(n):
    arr[i]=int(input())

#print(arr)

dp=[[[[[[[0 for _ in range(11)]
            for _ in range(11)]
                for _ in range(6)]
                    for _ in range(6)]
                        for _ in range(6)]
                            for _ in range(6)] 
                                for _ in range(6)]

def go(pprev,prev,a,b,c,d,e):
    
    if dp[pprev][prev][a][b][c][d][e] != 0:
        return dp[pprev][prev][a][b][c][d][e]
    if a==0 and b==0 and c==0 and d==0 and e==0:
        return 1
    
    if pprev!=0 and prev!=0 and a>0:
        dp[pprev][prev][a][b][c][d][e]+=go(prev,0,a-1,b,c,d,e)
    if pprev!=1 and prev!=1 and b>0:
        dp[pprev][prev][a][b][c][d][e]+=go(prev,1,a,b-1,c,d,e)
    if pprev!=2 and prev!=2 and c>0:
        dp[pprev][prev][a][b][c][d][e]+=go(prev,2,a,b,c-1,d,e)
    if pprev!=3 and prev!=3 and d>0:
        dp[pprev][prev][a][b][c][d][e]+=go(prev,3,a,b,c,d-1,e)
    if pprev!=4 and prev!=4 and e>0:
        dp[pprev][prev][a][b][c][d][e]+=go(prev,4,a,b,c,d,e-1)

    return dp[pprev][prev][a][b][c][d][e]
# print(arr)
print(go(5,5,arr[0],arr[1],arr[2],arr[3],arr[4]))

#print(dap)
