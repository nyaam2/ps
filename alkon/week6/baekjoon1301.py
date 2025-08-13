N=int(input())
remains=[int(input())for _ in range(N)]

dp={}

def dfs(remains:list,a:int,b:int):

    state=(*remains,a,b)
    if state in dp:
        return dp[state]
    
    if sum(remains)==0:
        return 1
    
    answer=0

    for x in range(N):
        if remains[x] and x!=a and x!=b:
            remains[x]-=1
            answer+=dfs(remains,b,x)
            remains[x]+=1
    dp[state]=answer
    return answer

print(dfs(remains,-2,1))