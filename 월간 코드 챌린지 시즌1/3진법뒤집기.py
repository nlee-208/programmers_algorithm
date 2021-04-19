# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    rem = []
    answer = 0
    while n > 0:
        rem.append(n % 3)
        n = n // 3
    rem.reverse()

    for i in range(len(rem)):
        answer += rem[i] * (3 ** i)

    return answer