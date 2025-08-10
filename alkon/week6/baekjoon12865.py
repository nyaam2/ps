import copy
n,k=map(int,input().split())
arr=[]
for i in range(n):
  a,b=map(int,input().split())
  arr.append((a,b))

result=[0]*(k+1)



for i in range(n):
  w,v=arr[i]
  # print(w,k)
  # if result[w]==0:
  #   result[w]=v
  
  visited=[False]*(k+1)
  
  # if w<=k and result[w]==0:
  #   result[w]=v
  #   visited[w]=True
  tmp=copy.copy(result)
  for j in range(0,k+1,1):
    # if result[j]!=0 and visited[j]==False:
      
      
      if j+w<=k:
        if j==0:
          visited[j+w]=True
          result[j+w]=max(tmp[j+w],tmp[j]+v)
        else:
          if result[j]==0:
            continue
          visited[j+w]=True
          result[j+w]=max(tmp[j+w],tmp[j]+v)

  
          
      
          
        
        
  # print(f"result : {result}")
  # print(f"visited { visited}")


dap=0
for i in range(1,k+1,1):
  if result[i]!=0 or result[i]!=0:

    dap=max(dap,result[i],result[i])
print(dap)
