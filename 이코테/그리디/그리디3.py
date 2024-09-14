# 입력 받은 숫자의 최대 수 구하기.
# input 3 0 2 2 1
# output 13
arrList = list(map(int, input()))
# arrList.sort(reverse=True)

total = 1
for i in arrList:
    if(i <= 1):
        total += i
    else:
        total *= i
print(total)