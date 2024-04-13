arr = [0, 0, 0, 0, 0, 0]
print(arr)

arr = [0] * 6
print(arr)

arr = list(range(6))
print(arr)

arr = [0 for _ in range(6)]
print(arr)


arr = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print(arr)

# list comprehension
arr = list(range(6))
print(arr)
squres = [num**2 for num in arr]
print(squres)

# sort
arr = [1, 3, 2, 5, 4]
print(arr)
sorted_arr = sorted(arr)
print(arr)
print(sorted_arr)
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

