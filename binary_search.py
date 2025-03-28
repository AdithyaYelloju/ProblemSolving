def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [2,3,4,2,3,4]
arr.sort()
print(arr)
target = 4
result = binary_search(arr, target)
print(result)
