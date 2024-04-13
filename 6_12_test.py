# 주식 가격

# 주식이 떨어지지 않은 기간을 구하기

# [1, 2, 3, 2, 3] 이면 [4, 3, 1, 1, 0]
# 1 은 4초동안 안 떨어짐
# 2 는 3초동안 안 떨어짐
# 3 은 1초동안 안 떨어짐
# 2 는 1초동안 안 떨어짐
# 3 은 0초동안 안 떨어짐



### 무식한 방법
# prices = [1, 2, 3, 2, 3]

# result = []
# for i in range(len(prices)):
#     up_count = 0
#     for j in range(i+1, len(prices)):
#         if prices[j] >= prices[i]:
#             up_count += 1
#         else:
#             if up_count == 0:
#                 up_count = 1
#             break
#     result.append(up_count)
# print(result)

### 효율적인 방법
prices = [1, 2, 3, 2, 3]

n = len(prices)
answer = [0] * n  # ➊ 가격이 떨어지지 않은 기간을 저장할 배열

# 스택(stack)을 사용해 이전 가격과 현재 가격을 비교
stack = [0]  # ➋ 스택 초기화
for i in range(1, n):
    while stack and prices[i] < prices[stack[-1]]:
      # ➌ 가격이 떨어졌으므로 이전 가격의 기간을 계산
      j = stack.pop( )
      answer[j] = i - j
    stack.append(i)
print(stack)

# ➍ 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
while stack:
    j = stack.pop( )
    answer[j] = n - 1 - j

print(answer)


