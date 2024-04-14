# 메뉴 리뉴얼

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

from itertools import combinations
from collections import Counter

# for it in combinations(orders[0], 2):
#     print(it)

answer = []

for c in course:
    menu = []
    for order in orders:
        comb = combinations(sorted(order), c)
        menu += comb
    # print(menu)

    counter = Counter(menu)
    print(counter)

    if (len(counter) != 0 and max(counter.values()) != 1):  # 가장 많은 주문이 1번 이상 주문된 경우
        for m, cnt in counter.items():
            if cnt == max(counter.values()):
                answer.append("".join(m))
print(sorted(answer))