def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 测试插入排序函数
arr = [64, 34, 25, 12, 22, 11, 90]
print("插入排序前的数组:", arr)
sorted_arr = insertion_sort(arr)
print("插入排序后的数组:", sorted_arr)
