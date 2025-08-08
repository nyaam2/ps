n=int(input())
for i in range(n):
    t=int(input())
    dp=[[-1]*7 for _ in range(t+2)]
    dp[1][1]=1 
    for j in range(2,t+2,1):
        o1,num1,o2,num2=map(str,input().split())
        for k in range(0,7,1):
            if dp[j-1][k]==-1:
                continue
            else:
                if o1=="+":
                    dp[j][(dp[j-1][k]+int(num1))%7]=(dp[j-1][k]+int(num1))%7
                elif o1=="*":
                    dp[j][(dp[j-1][k]*int(num1))%7]=(dp[j-1][k]*int(num1))%7

                if o2=="+":
                    dp[j][(dp[j-1][k]+int(num2))%7]=(dp[j-1][k]+int(num2))%7
                elif o2=="*":
                    dp[j][(dp[j-1][k]*int(num2))%7]=(dp[j-1][k]*int(num2))%7
    if dp[t+1][0]==0:
        print("LUCKY")
    else:
        print("UNLUCKY")
    
    