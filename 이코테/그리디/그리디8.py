import time


a = list(map(str, input()))
start = time.time()
# 문자열 재정렬
num = [str(i) for i in range(1, 11)]
# 리스트 컴프리헨션 if문 기억할 것!!!
isNum = [int(i) for i in a if i in num]
isStr = [str(i) for i in a if i not in num]
isStr.sort()

for i in isStr:
    print(i, end='')
print(sum(isNum))
end = time.time()
print(f"{end - start:.5f} sec")

### 풀이 ###
data = input()
start = time.time()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))
end = time.time()
print(f"{end - start:.5f} sec")