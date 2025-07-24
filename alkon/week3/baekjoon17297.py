m=int(input())

arr=[]
arr.append(len("Messi"))
arr.append(len("Messi Gimossi"))
while arr[-1]<pow(2,30)-1:
    a=arr[-1]
    b=arr[-2]
    arr.append(a+b+1)

size=len(arr)

def search(step,order):
    global arr
    if order<=arr[1]:
        return order
    if order<arr[step-1]:
        return search(step-1,order)
    elif order==arr[step-1]+1:
        return -1
    elif order>arr[step-1]:
        return search(step-2,order-arr[step-1]-1)
    
dap=search(size,m)
if dap==-1 or dap==6:
    print("Messi Messi Gimossi")
else:
    print("Messi Gimossi"[dap-1])
