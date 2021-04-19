# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort(reverse=1)
    summed = sum(d)
    answer = len(d)

    for i in d:
        if summed <= budget:
            break
        summed -= i
        answer -= 1

    return answer