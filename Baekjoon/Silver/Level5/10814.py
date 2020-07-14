# silver 5 나이순 정렬

N = int(input())
peoples = []

for i in range(N):
    age, name = input().split()
    peoples.append((int(age), i, name))

peoples.sort()

for people in peoples:
    print('{} {}'.format(people[0], people[2]))