# bronze 2 상수

user_input = input().split()

user_input[0] = int(user_input[0][::-1])
user_input[1] = int(user_input[1][::-1])

if user_input[0] > user_input[1]:
    print(user_input[0])
else:
    print(user_input[1])