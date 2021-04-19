# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    def binary(num):
        answer = []
        while num > 1:
            answer.append(num % 2)
            num = num // 2
        answer.append(num % 2)

        while len(answer) < n:
            answer.append(0)

        answer.reverse()
        return answer

    answer = []
    for i in range(n):
        temp = ''
        temp1 = binary(arr1[i])
        temp2 = binary(arr2[i])
        for j in range(n):
            if temp1[j] + temp2[j] >= 1:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer