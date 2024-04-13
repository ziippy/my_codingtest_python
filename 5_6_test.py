# 실패율 : 스테이지에 도달했으나 클리어하지 못한 플레이 수 / 스테이지에 도달한 플레이어 수

# 입력
# N 개의 스테이지
# 현재 멈춰 있는 스테이지 번호가 담긴 배열
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 리턴
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# N = 4
# stages = [4, 4, 4, 4, 4]

fail_rates = []
for i in range(1, N + 1):
    reach_count = 0
    stay_count = 0
    for stage in stages:
        if stage >= i:
            reach_count += 1
        if stage == i:
            stay_count += 1
    #
    fail_rate = 0
    if stay_count > 0:
        fail_rate = stay_count / reach_count
    fail_rates.append(fail_rate)
    print("stage " + str(i) + " stay_count " + str(stay_count) + " reach_count " + str(reach_count) + " fail_rate " + str(fail_rate))

print(fail_rates)
# print(sorted(fail_rates, reverse=True))
indexed_values = list(enumerate(fail_rates))
print(indexed_values)
indexed_values.sort(key=lambda x: x[1], reverse=True)
print(indexed_values)

sorted_indices = [index + 1 for index, value in indexed_values]
print(sorted_indices)

