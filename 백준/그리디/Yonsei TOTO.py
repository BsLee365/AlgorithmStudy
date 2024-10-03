import sys
## 한번 더 복습 필요
n, m = map(int, sys.stdin.readline().split())

reg = []
s = 0
for _ in range(0, n):
    p, l = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    if p < l:
        reg.append(1)
    else:
        d.sort(reverse=True)
        reg.append(d[l - 1])
reg.sort()
for i in reg:
    if m - i >= 0:
        s += 1
        m -= i
print(s)
