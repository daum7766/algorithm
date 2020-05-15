def check(a):
    t = str(a)
    for i in t:
        a += int(t)
    if a < 10000:
        c_list[a] = 0

c_list = [1 for _ in range(10000)]
for i in range(1, 10000):
    if c_list[i]:
        check(i)
        print(i)
