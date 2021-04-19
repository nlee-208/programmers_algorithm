# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    answer = ''
    id = new_id
    id = id.lower()
    id = re.sub(r"[^a-z0-9-_.]", "", id)
    id = re.sub("\.+", ".", id)
    id = id.strip('.')

    if (len(id) == 0):
        id = 'a'

    if (len(id) >= 16):
        id = id[:15]
        id = id.rstrip('.')

    if (len(id) <= 2):
        id = id + id[-1] * (3 - len(id))

    answer = id

    return answer