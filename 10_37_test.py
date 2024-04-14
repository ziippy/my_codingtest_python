# 섬 연결하기

# costs 는 [섬, 섬, 비용] 의 모음으로 되어 있음
# 모두를 통행할 수 있는 최소 비용 구하기

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

# 사이클 여부를 알아내는 방법
# A 와 B 의 집합이 A 와 같은 경우 --- 사이클

# 접근 방법
# 비용별 오름차순 정렬
# 섬과 섬을 엮으면서 모든 섬이 연결되었는지 확인

sorted_cost = sorted(costs, key=lambda x: x[2])
print(sorted_cost)

all_island = set(range(n))
print(all_island)

money = 0
cur_island = set()
for cost in sorted_cost:
    # print(cost)
    money += cost[2]
    # cur_island.add(cost[0])
    # cur_island.add(cost[1])
    cur_island.update({cost[0], cost[1]})

    if all_island == cur_island:
        break

print(money)



