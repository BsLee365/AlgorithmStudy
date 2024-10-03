# 여행가 위치 구하기
# input 5
# input R R R U D D
# output 3 4

maxNum = int(input())
arrList = input().split()
now = [1, 1]

for i in arrList:
    # 이동 좌표로 움직임
    if i == 'L':
        now[1] = now[1] - 1
    elif i == 'R':
        now[1] = now[1] + 1
    elif i == 'U':
        now[0] = now[0] - 1
    elif i == 'D':
        now[0] = now[0] + 1
    # 공간을 벗어나면 무시
    if now[0] <= 0:
        now[0] = 1
        continue
    elif now[1] <= 0:
        now[1] = 1
        continue
    elif now[1] >= maxNum:
        now[1] = 5
        continue
    elif now[0] >= maxNum:
        now[0] = 5
        continue
print(now[0], now[1])


##### 정석 풀이 #####
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y, = nx, ny
print(x, y)