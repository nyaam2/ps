while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    arr=list(map(int,input().split()))
  
    dp=[[0 for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        dp[i][1]=1
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                for l in range(1,k+1,1):
                    dp[i][l]+=dp[j][l-1]
    dap=0
    for i in range(n):
        dap+=dp[i][k]

    print(dap)
            


    
