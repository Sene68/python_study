# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [['chi', 20.0], ['beta', 50.0], ['alpha', 50.0]]
# The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0.
# There are two students with that score: ['beta' , 'alpha']. Ordered alphabetically, the names are printed as:
# alpha
# beta
import operator

def print_nested_list(students):

    #숫자 오름차순 정렬
    scoreArr = sorted(students, key=operator.itemgetter(1))

    score_list = []
    #숫자만 따로 저장..
    for items in scoreArr:
        for idx, val in enumerate(items):
            if(idx == 1):
                score_list.append(items[idx])

    lower = score_list[0]
    #두번째로 낮은 점수 찾기
    for i in range(1, len(score_list)):
        if score_list[i] != lower:
            break


    # 두번째로 낮은 점수의 사람 찾아 정렬
    final = sorted([student[0] for student in students if student[1] == score_list[i]])

    #출력
    for item in final:
        print(item)


if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    print_nested_list(students)
