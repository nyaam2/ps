#처음에 생각했던 코드
# while True:
#     n,k=map(int,input().split())
#     if n==0 and k==0:
#         break
#     arr=list(map(int,input().split()))
    
#     dp=[[] for _ in range(100)]
#     dap=0


#     for i in range(n):
#         dp[i].append(1)
#         for j in range(0,i,1):
#             if arr[i]>arr[j]:
#                 for l in dp[j]:
#                     if l+1>=k:
#                         dap+=1
#                     dp[i].append(l+1)

#     print(dap)

while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    arr=list(map(int,input().split()))
    
    dp=[[0 for _ in range(100)] for _ in range(n)]
    for i in range(n):
        dp[i][1]=1
        for j in range(0,i,1):
            if arr[j]<arr[i]:
                for l in range(2,k+1,1):
                    dp[i][l]+=dp[j][l-1]
    
    dap=0
    for i in range(n):
        dap+=dp[i][k]
    print(dap)
