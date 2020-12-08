def findTheValue(arr,target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1
    
    
    

arr = [1,5,14,25,33,44,60]
target = 44

result = findTheValue(arr, target)
print(result)