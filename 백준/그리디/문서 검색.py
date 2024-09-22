num1 = input()
num2 = input()

cnt = 0
while True:
    if num2 == num1[0:len(num2)]:
        cnt += 1
        num1 = num1[len(num2):]
    else:
        num1 = num1[1:]
    if len(num1) < len(num2):
        break
print(cnt)


## 꽤 괜찮은 풀이 ##
doc = input()
word = input()
res = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break
    res += 1
    doc = doc[idx+len(word):]
print(res)