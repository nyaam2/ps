n=int(input())
arr=list(map(int,input().split()))  #학생들의 제기차기 점수
p,q,r,s=map(int,input().split())

arr.sort()

start=1
end=110000

mid=0
studentsSum=0
def getSum(k)->int:
    studentsSum=0
    global p,q,r
    for score in arr:
        if score<k:
            studentsSum+=score+q
        elif score>k+r:
            studentsSum+=score-p
        else:
            studentsSum+=score
    return studentsSum

flag=False
dap=30000000000
while start<=end:
    mid=start+(end-start)//2
    # print(f"mid의 값 : {mid}")
    tmpSum=getSum(mid)
    if tmpSum>=s:
        end=mid-1
        dap=min(dap,mid)
        flag=True
    elif tmpSum<s:
        start=mid+1
        

if flag:
    print(dap)
else:
    print(-1)

    
