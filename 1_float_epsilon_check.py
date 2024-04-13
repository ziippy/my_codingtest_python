import sys

print(sys.float_info.epsilon)

a = 0.1 + 0.1 + 0.1
b = 0.3
c = a - b

if c == 0:
    print("zero")
else:
    print("not zero")
# not zero 출력


if c < sys.float_info.epsilon:
    print("zero")
else:
    print("not zero")
# zero 출력