# bronze 1 펠린드롬 수

while True:
    user_input = input()
    if user_input == '0':
        break
    
    length = len(user_input)
    answer = 'yes'
    for i in range(length//2):
        if user_input[i] != user_input[length-1-i]:
            answer = 'no'
            break
    
    print(answer)