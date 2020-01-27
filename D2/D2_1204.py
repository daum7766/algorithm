t = int(input())
while t:
    t -= 1
    case = int(input())
    grade = input()
    grade = grade.split()
    grade = list(map(int, grade))
    lst = [0]*101
    for g in grade:
        lst[g] += 1
    for i in range(100, -1, -1):
        if max(lst) == lst[i]:
            print(f"#{case} {i}")
            break