import sys
'''
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
            # print('cnt > ', cnt, ' price > ', price, ' nlist[i] > ', nlist[i])
            price = (cnt * nlist[i]) - (-1*price)
            cnt = 0
    pricelist.append(price)

for i in pricelist:
    print(i, end=' ')
'''

# 다른 풀이
for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    answer = 0
    mx = data[-1]
    for i in range(n-2, -1, -1):
        if data[i] > mx:
            mx = data[i]
        else:
            answer += mx-data[i]
    print(answer)
