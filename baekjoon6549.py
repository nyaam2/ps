while True:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    heights=a[1:]
    heights.append(0)

    stack=[]
    max_area=0
    i=0

    while i<len(heights):
        if not stack or heights[stack[-1]]<=heights[i]:
            stack.append(i)
            i+=1
        else:
            top=stack.pop()
            width=i if not stack else i-stack[-1]-1
            area=heights[top]*width
            max_area=max(max_area,area)
    
    print(max_area)