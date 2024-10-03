import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    price = 0
    n = 0
    mx = 0
    n = int(input())
    nlist = list(map(int, input().split(' ')))
    for i in range(n-1, -1, -1):
        if mx < nlist[i]:
            mx = nlist[i]
        else:
            price = (mx - nlist[i]) + price
    print(price)
'''
# 이렇게 풀면 무조건 다음 가격이 현재가격이 비쌀경우 팔기 때문에 옳바르지 못한 알고리즘이다.
input = sys.stdin.readline
t = int(input())
pricelist = []
n = 0
for _ in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))

    cnt = 0
    price = 0
    for i in range(n):
        # 사고
        if i != n-1 and nlist[i] <= nlist[i+1]:
            cnt += 1
            price -= nlist[i]
        # 팔고
        else:
            price = (cnt * nlist[i]) - (-1*price)
            cnt = 0
    pricelist.append(price)

for i in pricelist:
    print(i, end=' ')
'''