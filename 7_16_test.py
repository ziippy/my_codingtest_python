# 기능 개발
# 기능별 진도율
# 기능별 개발 속도
# 배포 때마다 몇 개의 기능이 배포되는지 반환

from collections import deque
import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]

n = len(progresses)
# d = deque(progresses)
# print(d)

day_lefts = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
print(day_lefts)

max_day = day_lefts[0]

deploy_list = []

count = 0
for i in range(n):
    if day_lefts[i] <= max_day:
        count += 1
    else:
        deploy_list.append(count)
        count = 1
        max_day = day_lefts[i]

deploy_list.append(count)
print(deploy_list)


