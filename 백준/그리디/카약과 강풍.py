n = input()
s = input()
r = input()

listN = [i for i in range(1, len(n)+1)]
listS = list(map(int, s.split(' ')))
listR = list(map(int, r.split(' ')))

cantborrow = list(set(listS) & set(listR))
listS = [i for i in listS if i not in cantborrow]
listR = [i for i in listR if i not in cantborrow]

ori_listR = listR.copy()

for i in listR:
    if i-1 in listS:
        listS.remove(i-1)
        ori_listR.remove(i)
    elif i+1 in listS:
        listS.remove(i+1)
        ori_listR.remove(i)
print(len(listS))