import math
from decimal import Decimal, getcontext, ROUND_HALF_UP

a,b,c=map(int,input().split())

left=0
right=40_000 #10만/pi을 rough하게 4만으로 잡음.
x=1/ Decimal('7')
# print(1/Decimal(str(x)))
# print(x)
t=0
while left<=right:
    mid=left+(right-left)//2
    p=math.pi
    if b*math.sin(mid*p)<=-a*mid*p+c:
        left=mid+1
        t=mid
    elif b*math.sin(mid*p)>-a*mid*p+c:
        right=mid-1

left=t*Decimal(math.pi)
right=(t+1)*Decimal(math.pi)

# print(((left+right))/2)
dap=0
while left<=right:
    mid=left+(right-left)/2
    if b*math.sin(mid)<=-a*mid+c:
        left=mid+Decimal(0.00000000001)
        dap=mid
    elif b*math.sin(mid)>-a*mid+c:
        right=mid-Decimal(0.00000000001)


print(dap)
    



