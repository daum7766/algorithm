#B3 2884 알람시계

hour, minute = map(int, input().split())

time = 24*60 + hour*60 + minute
time -= 45
hour = (time//60) % 24
minute = time % 60

print('{} {}'.format(hour, minute))