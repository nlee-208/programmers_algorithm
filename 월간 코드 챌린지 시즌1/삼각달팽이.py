# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2, 3]

    answer = []
    dir = [0, 1, 2] * (n // 3)  # 아래 오른 대각상승
    dir = dir[:n]
    pos = [0, 0]

    num = list(range(1, sum(range(1, n + 1)) + 1))
    end = list(range(n, 0, -1))

    list_ = [[0] * n for i in range(n)]
    list_[0][0] = 1

    i = 0
    end_ = 0

    while i < max(num):
        for d in dir:
            t = 0
            while t < end[end_]:
                if d == 0:
                    list_[pos[0]][pos[1]] = num[i]
                    pos[0] += 1
                    i += 1
                    t += 1

                    if t == end[end_]:
                        pos[0] -= 1
                        pos[1] += 1

                elif d == 1:
                    list_[pos[0]][pos[1]] = num[i]
                    pos[1] += 1
                    i += 1
                    t += 1

                    if t == end[end_]:
                        pos[0] -= 1
                        pos[1] -= 2

                else:
                    list_[pos[0]][pos[1]] = num[i]
                    pos[0] -= 1
                    pos[1] -= 1
                    i += 1
                    t += 1

                    if t == end[end_]:
                        pos[0] += 2
                        pos[1] += 1

            end_ += 1
            if end_ >= n:
                break

    for s in list_:
        answer += s

    return [x for x in answer if x > 0]