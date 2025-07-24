n=int(input())

visited=[False for _ in range(n)]
diag1=[False for _ in range(2*n)]
diag2=[False for _ in range(2*n)]
dap=0
def go(row):
    global dap

    if row==n:
        dap+=1
        return
    for c in range(n):
        if not visited[c] and not diag1[row+c] and not diag2[row-c+n]:
            visited[c]=diag1[row+c]=diag2[row-c+n]=True
            go(row+1)
            visited[c]=diag1[row+c]=diag2[row-c+n]=False

go(0)
print(dap)

            