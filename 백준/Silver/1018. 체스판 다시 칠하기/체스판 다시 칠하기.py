import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    board.append(line)

answer_list = []
new_board = []

for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        W += 1
                    if board[k][l] != 'B':
                        B += 1
                else:
                    if board[k][l] != 'B':
                        W += 1
                    if board[k][l] != 'W':
                        B += 1
        answer_list.append(W)
        answer_list.append(B)

print(min(answer_list))
