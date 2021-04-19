# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    n = len(numbers)
    frame = []
    answer = []
    for i in range(n-2):
      for j in range(i+1,n):
        frame.append(numbers[i]+numbers[j])
    frame.sort()

    for item in frame:
      if item not in answer:
        answer.append(item)
    return answer