from itertools import combinations

n,m,r=map(int,input().split())

arr=[] #말뚝 list
arr=list(map(int,input().split()))

arr2=[] #깃대 list
arr2=list(map(int,input().split()))

arr3=set() #말뚝 조합 set
for comb in combinations(arr,2):
    arr3.add(abs(comb[0]-comb[1]))


arr2.sort()


dap=[]

for i in arr3:
 
    start=0
    end=len(arr2)-1
    mid=0
    while start<=end: # =붙여야 되는 거 주의!
        mid=(end-start)//2+start
 
        if float(r)<float(arr2[mid]*i/2):
            end=mid-1
        elif float(r)>float(arr2[mid]*i/2):
            dap.append(round(float((arr2[mid]*i)/2),1)) #r값보다 작을 때만 넣어주어야 하기 때문에 이 조건문에 넣어줌.
                                                        #만일 while문이 끝나고 넣어주면, r값보다 큰 값이 들어갈 수도 있음. 또한 r값보다 작은 값이 무시될 수도 있기 때문에 이때 넣어주어야 함.
            start=mid+1
        else:
            print(round(float(r),1))
            exit()

    

dap.sort()
idx=0
if len(dap)==0:
    print(-1)
    exit()
for i in range(len(dap)):
    if i==0 and dap[i]>r:
        print(-1)
        exit()
    if dap[i]<r:
        idx+=1
    else:
        print(dap[idx-1])
        exit()
print(dap[-1])




