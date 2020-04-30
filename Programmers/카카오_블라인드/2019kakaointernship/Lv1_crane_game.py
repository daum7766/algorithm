#프로그래머스 2019 카카오 개발자 겨울 인턴십
#크레인 인형뽑기 게임

#스택확인함수
def stack_check(stack, item):
    #스택의 탑과 아이템이 같다면 꺼내서 삭제
    if stack and stack[-1] == item:
        stack.pop()
        return 2
    #아니라면 아이템 추가
    stack.append(item)
    return 0


def solution(board, moves):
    answer = 0
    stack = []
    #몇번째 칸에 인형이 어디까지 차있는지 저장하는 변수
    board_check = [-1 for _ in range(30)]
    N = len(board)
    for m in moves:
        #인형이 없다면 넘어간다.
        if board_check[m-1] == N:
            continue
        #탐색을 한번도 하지 않았다면
        elif board_check[m-1] == -1:
            #제일 위에서부터 탐색
            for i in range(N):
                # 보드값이 0이 아니라면
                if board[i][m-1]:
                    # 인형을 뺄꺼나까 값을 미리 한칸 추가하고
                    board_check[m-1] = i+1
                    #스택검사를 해서 확인
                    answer += stack_check(stack, board[i][m-1])
                    #인형은 뽑았으니까 데이터를 0으로 바꿔줌
                    board[i][m-1] = 0
                    break
        #이미 확인한 기록이 있다면
        elif board_check[m-1]:
            #너무 길어지니까 인덱스 꺼내서
            idx = board_check[m-1]
            #검사하는 함수돌리고
            answer += stack_check(stack, board[idx][m-1])
            #뽑았으니까 데이터 0으로 바꾸고
            board[idx][m-1] = 0
            #인덱스 위치 조정
            board_check[m-1] += 1
    #결과값 리턴
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))