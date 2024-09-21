# 나이트가 이동할 확률

row = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
now = list(map(str, input()))
now = [row[now[0]], int(now[1])]

# L R U D
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

temploc = now.copy()
# x 축 탐색
for i in range(0, 2):
    temploc = now.copy()
    temploc[0] = temploc[0] + dx[i] + dx[i]
    for j in range(2, 4):
        temploc[1] = temploc[1] + dy[j]
        if temploc[0] > 0 and temploc[1] > 0:
            cnt += 1
        temploc[0] = now[0]
# 좌표 초기화
temploc = now.copy()
# y축 탐색
for i in range(2, 4):
    temploc = now.copy()
    temploc[1] = temploc[1] + dy[i] + dy[i]
    for j in range(0, 2):
        temploc[0] = temploc[0] + dx[j]
        if temploc[0] > 0 and temploc[1] > 0:
            cnt += 1
        temploc[1] = now[1]
print(cnt)
