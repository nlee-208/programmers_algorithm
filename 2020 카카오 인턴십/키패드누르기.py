# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    x = [1] + [0, 1, 2] * 3 + [0, 2]
    y = [0, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0]
    answer = ''
    temp_L = 10;
    temp_R = 11
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            temp_L = i

        if i in [3, 6, 9]:
            answer += 'R'
            temp_R = i

        if i in [2, 5, 8, 0]:
            if (abs(x[temp_L] - x[i]) + abs(y[temp_L] - y[i])) == (abs(x[temp_R] - x[i]) + abs(y[temp_R] - y[i])):
                if hand == 'left':
                    answer += 'L'
                    temp_L = i
                else:
                    answer += 'R'
                    temp_R = i

            elif (abs(x[temp_L] - x[i]) + abs(y[temp_L] - y[i])) > (abs(x[temp_R] - x[i]) + abs(y[temp_R] - y[i])):
                answer += 'R'
                temp_R = i

            else:
                answer += 'L'
                temp_L = i
    return answer