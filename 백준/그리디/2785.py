'''
풀이과정
체인을 하나씩 소모하면서 몇개 연결했는지 카운트하면 된다.
연결을 할때는 뒤에 가장 큰 수부터 연결해주면 된다.
'''

import sys

input = sys.stdin.readline
n = int(input())
chains = list(map(int, input().split(' ')))
chains.sort()
count = 0
for chain in chains:
    i = chain
    while True:
        # 묶을 체인이 없다면,
        if len(chains) == 1:
            break
        # 체인을 묶는다
        chains[-1] = chains[-1] + chains[-2]
        chains = chains[:-2]
        chains.append((chains[-1]))
        # 체인을 하나 감소시킨다.
        i -= 1
        count += 1

print(count)
