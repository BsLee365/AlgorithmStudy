import time
# 시각 문제
# 정수 N을 입력받아 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
n = int(input())
start_time = time.time()
hour, min, sec = 0, 0, 0
cnt = 0
while True:
    sec += 1
    if sec == 60:
        min += 1
        sec = 0
    elif min == 60:
        hour += 1
        min = 0
    if '3' in str(sec) + str(min) + str(hour):
        cnt += 1
        # print(hour, ':', min, ':', sec)
    if hour > n:
        break
    # print(hour, ':', min, ':', sec)
print(cnt)
end_time = time.time()
print(f"실행 시간: {end_time - start_time:.6f} 초")

#### 해답 ####
h = int(input())
start_time = time.time()
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                # print(i, ':', j, ':', k)
print(count)
end_time = time.time()
print(f"실행 시간: {end_time - start_time:.6f} 초")