# 방문 길이

# 이전에 방문한 길은 무시

# U = 위로 한 칸
# D = 아래로 한 칸
# R = 오른쪽으로 한 칸
# L = 왼쪽으로 한 칸

# 좌표평면 -5,-5 부터 5,5 까지다. 시작은 0,0 이다.

# ==> 0,0 부터 10,10 으로 생각하면 된다. 시작은 5,5 로 생각하면 된다.

dirs = "ULURRDLLU"
# dirs = "LULLLLLLU"

all_dirs = [[0 for _ in range(10)] for _ in range(10)]
# print(all_dirs)

x = 4
y = 4
all_dirs[x][y] = 1  # 처음 시작은 거쳐서 갔음 으로 표시 (1로 표시)

new_dir = 1

def is_valid(x, y):
    return 0 <= x < 10 and 0 <= y < 10

def update_if_new(x, y):
    if all_dirs[x][y] == 0:
        all_dirs[x][y] = 1
        global new_dir
        new_dir += 1

for dir in dirs:
    tmp_x, tmp_y = x, y
    if dir == 'U':
        tmp_y += 1
    elif dir == 'D':
        tmp_y -= 1
    elif dir == 'R':
        tmp_x += 1
    elif dir == 'L':
        tmp_x -= 1
    if is_valid(tmp_x, tmp_y):
        x, y = tmp_x, tmp_y
        update_if_new(x, y)
    # print(x, y)

print(new_dir)