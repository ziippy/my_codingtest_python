# 크레인 인형 뽑기 게임

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

# board -> stack
n = len(board)

stacks = [[] for _ in range(n)]

for i in range(n):
    for j in range(4, -1, -1):
        _tmp = board[j][i]
        if _tmp != 0:
            stacks[i].append(_tmp)

print(stacks)

moves = [1, 5, 3, 5, 1, 2, 1, 4]

dolls = []
boom_doll_count = 0

for move in moves:
    real_move = move - 1
    if stacks[real_move]:
        pick = stacks[real_move].pop()
        #
        if dolls and dolls[-1] == pick:
            dolls.pop()
            boom_doll_count += 2
        else:
            dolls.append(pick)

print(dolls)
print(boom_doll_count)