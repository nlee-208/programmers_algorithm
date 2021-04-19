# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = [0]
    count = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] >0:
                if answer[-1] == board[j][i-1]:
                    board[j][i-1] *=0
                    answer = answer[:-1]
                    count += 2
                else:
                    answer.append(board[j][i-1])
                    board[j][i-1] *=0
                break
    return count