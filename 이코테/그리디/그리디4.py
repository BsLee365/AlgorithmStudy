# 모험가 - 그리디 알고리즘

n = int(input())

arrList = list(map(int, input().split()))

arrList.sort()

group = 0 # 현재 그룹의 공포도
groupCnt = 0 # 현재 그룹의 수
for i in arrList:
    group += i
    if group < n:
        continue
    else:
        group = 0
        groupCnt += 1
print(groupCnt)