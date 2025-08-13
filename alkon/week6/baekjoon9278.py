import sys

MOD = 1_000_000
out = []

for s in sys.stdin.read().splitlines():
    if not s:
        continue
    n = len(s)
    h = n // 2

    # v[i][j] = 앞에서 i명 처리했을 때 50원 잔고가 j개인 경우의 수
    v = [[0] * (h + 1) for _ in range(n)]

    # 첫 문자가 ')'면 불가능
    if s[0] == ')':
        out.append("0")
        continue
    else:
        v[0][1] = 1  # '(' 또는 '.'이라면 첫 사람은 50만 가능

    for i in range(1, n):
        c = s[i]
        if c == ')':  # 100원 고정: j <- j+1
            for j in range(0, h):
                v[i][j] = (v[i][j] + v[i-1][j+1]) % MOD
        elif c == '(':  # 50원 고정: j <- j-1
            for j in range(1, h + 1):
                v[i][j] = (v[i][j] + v[i-1][j-1]) % MOD
        else:  # '.' 자유: 두 경우 모두 가능
            for j in range(1, h + 1):        # 50원 선택
                v[i][j] = (v[i][j] + v[i-1][j-1]) % MOD
            for j in range(0, h):            # 100원 선택
                v[i][j] = (v[i][j] + v[i-1][j+1]) % MOD


    out.append(str(v[n-1][0] % MOD))
 
print("\n".join(out))
