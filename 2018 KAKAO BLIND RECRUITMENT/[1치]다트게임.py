# https://programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution(dartResult):
    answer = [0] * 3
    case = 1
    trial = 0
    dart = [x for x in re.split('([#*SDT])', dartResult) if len(x) > 0]

    for i in range(len(dart)):
        if case == 1:
            temp = int(dart[i]);
            case += 1

        elif case == 2:
            if dart[i] == 'D':
                temp = temp ** 2

            elif dart[i] == 'T':
                temp = temp ** 3

            if i == len(dart) - 1:
                answer[trial] = temp
            case += 1

        else:
            if dart[i] in '*#':
                if dart[i] == '*':
                    if i == 2:
                        answer[trial] = temp * 2
                    else:
                        answer[trial - 1] *= 2
                        answer[trial] = temp * 2
                else:
                    answer[trial] = -temp
                case = 1
            else:
                answer[trial] = temp
                temp = int(dart[i])
                case = 2
            trial += 1

    return sum(answer)