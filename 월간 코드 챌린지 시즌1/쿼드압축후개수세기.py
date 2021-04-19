# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    a, b = 0, 0
    n = int(len(arr) / 2)
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []

    for i in range(n):
        for j in range(n):
            temp1.append(arr[i][j])
            temp2.append(arr[i][j + n])
            temp3.append(arr[i + n][j])
            temp4.append(arr[i + n][j + n])
    # exceptions
    total_sum = sum(temp1 + temp2 + temp3 + temp4)
    if total_sum == 0:
        return [1, 0]
    if total_sum == (n * 2) ** 2:
        return [0, 1]

    for j in [temp1, temp2, temp3, temp4]:
        if sum(j) == n ** 2:
            b += 1
        elif sum(j) == 0:
            a += 1
        elif n == 2:
            a += 4 - sum(j)
            b += sum(j)
        else:
            temp = solution([j[n * i: n * (i + 1)] for i in range(n)])
            a += temp[0]
            b += temp[1]

    return [a, b]