def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):  # 反向遍历
        for j in range(0,i):  # 由于最右侧的值已经有序，不再比较，每次都减少遍历次数
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubbleSort([9,8,7,6,5,4,3,2,1]))
