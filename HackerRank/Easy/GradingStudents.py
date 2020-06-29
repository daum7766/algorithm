grades_count = 4

grades = [73, 67, 38, 33]


def gradingStudents(grades):
    answer = []
    for i in range(grades_count):
        k = grades[i]
        temp = k
        a = k % 5
        if k >= 38 and a >= 3:
            temp = k + (5 - a)
        answer.append(temp)
    return answer