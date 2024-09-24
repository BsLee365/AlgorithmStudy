team = int(input())
skills = list(map(int, input().split(' ')))
skills.sort()
start = skills[:len(skills)//2]
end = skills[len(skills)//2:]

teamList = []
for i in range(0, team):
    teamList.append(start[i] +end[-(i+1)])
teamList.sort()
print(teamList[0])