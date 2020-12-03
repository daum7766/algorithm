# D2 1974 스도쿠 검증
sudoku_size = 9

def row_column_check(sudoku):
    for i in range(sudoku_size):
        row_validate = [0 for _ in range(sudoku_size)]
        column_validate = [0 for _ in range(sudoku_size)]
        for j in range(sudoku_size):
            row_number = sudoku[i][j] - 1 
            column_number = sudoku[j][i] - 1
            if row_validate[row_number] == 1 or column_validate[column_number] == 1:
                return False
            row_validate[row_number] = 1
            column_validate[column_number] = 1
    return True


def three_by_three_check(start_y, start_x, sudoku):
    validate = [0 for _ in range(sudoku_size)]
    for i in range(start_y, start_y+3):
        for j in range(start_x, start_x+3):
            number = sudoku[i][j] - 1
            if validate[number] == 1:
                return False
            validate[number] = 1
    return True


def solution(sudoku):
    if row_column_check(sudoku) == False:
        return 0
    for i in range(0, sudoku_size, 3):
        for j in range(0, sudoku_size, 3):
            if three_by_three_check(i, j, sudoku) == False:
                return 0
    return 1


for t in range(int(input())):
    sudoku = [list(map(int, input().split())) for _ in range(sudoku_size)]
    answer = solution(sudoku)

    print('#{} {}'.format(t+1, answer))