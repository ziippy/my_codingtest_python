# 표 편집

# 주어진 표에서
# U X 는 X칸 위에 있는 행을 선택
# D X 는 X칸 아래에 있는 행을 선택
# C 는 선택한 행 삭제 (이후 밑에 있는 행 선택, 만약 맨 밑이면 위에 있는 행 선택)
# Z 는 이전에 삭제한 것 복구

n = 8   # 8개 행 (원본)
k = 2   # 현재 선택된 행
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]

##########
# 현재 커서와 상관없이, 각 행별로 위 아래 행이 무엇인지를 담고 있는 배열 정의
# 0 번째와 맨 마지막번째를 위하여 위 아래로 행을 1개씩 추가

up = [i - 1 for i in range(n + 2)]
down = [i + 1 for i in range(n + 2)]

print(up)
print(down)

# ➌ 현재 위치를 나타내는 인덱스
k += 1

# 삭제한 것 보관 (스택)
deleted = [ ]

# ➍ 주어진 명령어(cmd) 리스트를 하나씩 처리
for cmd_i in cmd:
    # ➎ 현재 위치를 삭제하고 그다음 위치로 이동
    if cmd_i.startswith("C"):
        deleted.append(k)
        up[down[k]] = up[k]
        down[up[k]] = down[k]
        k = up[k] if n < down[k] else down[k]

    # ➏ 가장 최근에 삭제된 행을 복원
    elif cmd_i.startswith("Z"):
        restore = deleted.pop()
        down[up[restore]] = restore
        up[down[restore]] = restore

    # ➐ U 또는 D를 사용해 현재 위치를 위아래로 이동
    else:
        action, num = cmd_i.split()
        if action == "U":
            for _ in range(int(num)):
                k = up[k]
        else:
            for _ in range(int(num)):
                k = down[k]

# ➑ 삭제된 행의 위치에 'X'를, 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
answer = ["O"] * n
for i in deleted:
    answer[i - 1] = "X"
print("".join(answer))