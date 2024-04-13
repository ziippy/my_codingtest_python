# 인덱스가 다른 두 개 뽑아서 더하기
# 모든 수를 배열에 오름차순으로 담기

numbers = [2, 1, 3, 4, 1]

sum_list = []

n = len(numbers)
for i in range(n):
    for j in range(i+1, n):
        sum = numbers[i] + numbers[j]
        sum_list.append(sum)

print(sum_list)

sum_list = list(set(sum_list))
sum_list_final = sorted(sum_list)
print(sum_list_final)
