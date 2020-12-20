import base64

test_case_size = int(input())
for t in range(test_case_size):
    answer = str(base64.b64decode(input().encode('utf-8')))[2:-1]
    print('#{} {}'.format(t+1, answer))