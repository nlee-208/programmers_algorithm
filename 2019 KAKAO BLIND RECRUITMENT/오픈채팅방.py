# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nick2name = {}

    for i in record:
        spl = i.split(" ")
        if spl[0] == 'Enter':
            nick2name[spl[1]] = spl[2]

        if spl[0] == 'Change':
            nick2name[spl[1]] = spl[2]

    for i in record:
        spl = i.split(" ")
        if spl[0] == 'Enter':
            answer.append(f'{nick2name[spl[1]]}님이 들어왔습니다.')

        if spl[0] == 'Leave':
            answer.append(f'{nick2name[spl[1]]}님이 나갔습니다.')

    return answer