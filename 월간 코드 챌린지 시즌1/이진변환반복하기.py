# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    def binary(num):
        string = ''
        while num > 1:
            string += str(num % 2)
            num = num // 2
        string += str(num)
        return string[::-1]

    count = 0
    zeros = 0

    while s != '1':
        n = len([''.join(i) for i in s if i == '1'])
        count += 1;
        zeros += len(s) - n
        s = binary(n)

    return [count, zeros]