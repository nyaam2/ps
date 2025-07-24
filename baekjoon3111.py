import sys
input = sys.stdin.readline

A = input().strip()
T = input().strip()

lenA = len(A)
if lenA == 0:
    print(T)
    exit()

A_list = list(A)
A_rev = A_list[::-1]

left_stack = []
right_stack = []

l, r = 0, len(T) - 1
toggle = True

while l <= r:
    if toggle:
        left_stack.append(T[l])
        l += 1
        while len(left_stack) >= lenA and left_stack[-lenA:] == A_list:
            del left_stack[-lenA:]
    else:
        right_stack.append(T[r])
        r -= 1
        while len(right_stack) >= lenA and right_stack[-lenA:] == A_rev:
            del right_stack[-lenA:]
    toggle = not toggle

mid = left_stack + right_stack[::-1]

res_stack = []
for ch in mid:
    res_stack.append(ch)
    while len(res_stack) >= lenA and res_stack[-lenA:] == A_list:
        del res_stack[-lenA:]

print(''.join(res_stack))
