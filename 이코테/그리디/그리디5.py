# 여행가 위치 구하기
# input R R R U D D
# output 3 4

arrList = input().split()
now = [1, 1]

for i in arrList:

    if now[0] <= 0:
        now[0] = 1
        print(now[0])
        continue
    elif now[1] <= 0:
        now[1] = 1
        continue
    else:
        if i == 'L':
            now[1] = now[1] - 1
        elif i == 'R':
            now[1] = now[1] + 1
        elif i == 'U':
            now[0] = now[0] - 1
        elif i == 'D':
            now[0] = now[0] + 1

print(now)