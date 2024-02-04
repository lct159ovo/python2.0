def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# 测试快速排序函数
arr = [64, 34, 25, 12, 22, 11, 90]
print("快速排序前的数组:", arr)
sorted_arr = quick_sort(arr)
print("快速排序后的数组:", sorted_arr)