# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    rate = [0] * N

    for i in range(0, N):
        if i + 1 not in stages:
            rate[i] = 0

        else:
            rate[i] = len([x for x in stages if x == i + 1]) / len([x for x in stages if x >= i + 1])

    success = [1 - x for x in rate]
    list_ = sorted(list(zip(success, range(1, N + 1))))

    return [list_[i][1] for i in range(N)]