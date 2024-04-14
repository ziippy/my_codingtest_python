# 요세푸스 문제

# N명의 사람이 원 형태로 서 있음
# K 번째 사람을 없앰
# 없앤 사람 다음을 기준으로 하고 다시 K 번째 사람을 없앰
# 마지막에 살아있는 사람의 번호를 반환

from collections import deque

N = 5
K = 2

d = deque(range(1, N + 1))
print(d)

# for i in range(1, K):
#     d.append(d.popleft())
# d.popleft()
# print(d)

while len(d) > 1:
    for i in range(1, K):
        d.append(d.popleft())
    d.popleft()
    print(d)

print(d.popleft())


