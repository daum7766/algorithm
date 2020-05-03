#Lv3 카카오 2019 인턴십 불량이용자

def solution(user_id, banned_id):
    answer = set()
    ban_length = len(banned_id)
    user_length = len(user_id)
    if ban_length == user_length:
        return 1
    use_user = [1 for _ in range(user_length)]
    use_ban = [1 for _ in range(ban_length)]
    stack = []
    stack.append([0, use_user, use_ban])
    while stack:
        idx, use_user, use_ban = stack.pop()
        if idx == ban_length:
            temp = []
            for i in range(user_length):
                if not use_user[i]: temp.append(user_id[i])
            if temp: answer.add(tuple(temp))
        for i in range(ban_length):
            if use_ban[i] : 
                for j in range(user_length):
                    if use_user[j] and len(banned_id[i]) == len(user_id[j]):
                        for k in range(len(user_id[j])):
                            if user_id[j][k] != banned_id[i][k] and banned_id[i][k] != '*':
                                break
                        else:
                            use_user[j] = 0
                            use_ban[i] = 0
                            stack.append([idx+1, use_user[:], use_ban[:]])
                            use_user[j] = 1
                            use_ban[i] = 1
    return len(answer)

    
users_id = [
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"]
]

banned_id = [
    ["fr*d*", "abc1**"],
    ["*rodo", "*rodo", "******"],
    ["fr*d*", "*rodo", "******", "******"]
]

result = [2, 2, 3]

for i in range(3):
    answer = solution(users_id[i], banned_id[i])
    if answer == result[i]:
        print('정답')
    else:
        print('틀림')