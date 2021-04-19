# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    lis_ = []
    answer = 0

    for i in skill_trees:
        a = ''
        for j in range(len(i)):
            if i[j] in skill:
                a += i[j]
        lis_.append(a)

        if a == '':
            answer += 1
            lis_.remove(a)

    for k in lis_:
        if len(k) > 0:
            if k[0] == skill[0]:
                if k in skill:
                    answer += 1

    return answer