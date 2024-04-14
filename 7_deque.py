from collections import deque

d = deque(maxlen=5)

print(d)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)

print(d)

d.append(6)

print(d)

d.popleft()
print(d)

d.pop()
print(d)

################
import time

lst = list(range(100000))
dq = deque(range(100000))

# pop(0) 성능 측정
start = time.time()
for i in range(100000):
    lst.pop(0)
end = time.time()
print(end - start)

start = time.time()
for i in range(100000):
    dq.popleft()
end = time.time()
print(end - start)