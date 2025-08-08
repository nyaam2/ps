import sys
input = sys.stdin.readline
n, k = map(int, input().split())
seen = [0]*(k+1)
cnt = blocks = 0

for _ in range(n):
    x = int(input().strip())
    if not seen[x]:
        cnt += 1
    seen[x] = 1
    if cnt == k: 
        blocks += 1
        cnt = 0
        seen = [0]*(k+1)

print(blocks + 1)