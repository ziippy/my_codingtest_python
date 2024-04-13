import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def do_sort(arr):
    arr.sort()
    return arr


def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result


arr = list(range(10000))
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print('bubble_time:', bubble_time)

arr = list(range(10000))
sort_time, sort_result = measure_time(do_sort, arr)
print('sort_time:', sort_time)

print(bubble_result == sort_result)
