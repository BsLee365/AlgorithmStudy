a = list(map(int, input().split(' ')))
# 한블럭씩
home = [a[0], a[1]]
distance = []

# 대각선이 거리가 더 짧으면 대각선으로 최대한 감.
if home[0] + home[1] % 2 != 0 and a[2] >= a[3]:
    # 대각선으로 갈 수 있는 최대한 감.
    vec1 = max(home) - 1
    # 그 다음 직선으로 이동
    vec2 = max(home) - vec1
    vec1 = vec1 * a[3]
    vec2 = vec2 * a[2]
    vec = vec1 + vec2
    distance.append(vec)

# 직선 거리가 더 짧으면 대각선으로 최대한 짧게 간다음 직선으로 이동
elif home[0] + home[1] % 2 != 0 and a[2] <= a[3]:
    x = home[0]
    y = home[1]
    cnt = min(home)
    maxVec = cnt * a[3]
    o = maxVec + ((max(home) - cnt) * a[2])
    distance.append(o)

# 직선으로만 갔을 때
distance.append((a[0] + a[1]) * a[2])

# 대각선으로만 갔을 때
if (home[0] + home[1]) % 2 == 0:
    vec3 = max(home) * a[3]
    distance.append(vec3)

# 최소 길이만 출력.
print(min(distance))