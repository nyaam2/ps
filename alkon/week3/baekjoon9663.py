n=int(input())

col=[False for _ in range(n)]
diag1=[False for _ in range(2*n)] #/
diag2=[False for _ in range(2*n)] #\
dap=0
def go(row):
    global dap

    if row==n:
        dap+=1
        return
    for c in range(n):
        if not col[c] and not diag1[row+c] and not diag2[row-c+n]:
            col[c]=diag1[row+c]=diag2[row-c+n]=True
            go(row+1)
            col[c]=diag1[row+c]=diag2[row-c+n]=False

