def star(N,i,j):
    if (i//N)%3==1 and (j//N)%3==1:
        print(" ",end="")
    else:
        if N//3!=0:
            star(N//3,i,j)
        else:
            print("*",end="")

n=int(input())
for i in range(n):
    for j in range(n):
        star(n,i,j)
    print()