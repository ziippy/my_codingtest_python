# 백트래킹

# 1부터 N까지 숫자 중 합이 10이 되는 조합 구하기

# 백트래킹을 활용해야 함
# 숫자 조합은 오름차순으로 정렬
# 같은 숫자는 한번만 선택

N = 5

results = []

def backtrack(sum, selected_num, start):
    if sum == 10:
        results.append(selected_num)
        return

    for i in range(start, N + 1):
        if sum + i <= 10:
            backtrack(sum + i, selected_num + [i], i + 1)

backtrack(0, [], 1)

print(results)