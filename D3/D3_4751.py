#D3 4751 다솔이의 다이아몬드 장식
T = int(input())
for i in range(T):
    t = input()
    n = len(t)
    f = '..' + '...'.join('#'*n) + '..'
    s = '.#'*(n*2)+'.'
    t = '#.' + '.#.'.join(t) + '.#'
    print("{0}\n{1}\n{2}\n{1}\n{0}".format(f,s,t))