# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
from math import sqrt, floor


def solution(nums):
    candidates = [sum(x) for x in list(combinations(nums, 3))]
    answer = len(candidates)

    for i in candidates:
        for j in range(2, floor(sqrt(i)) + 1):
            if i % j == 0:
                answer -= 1
                break

    return answer