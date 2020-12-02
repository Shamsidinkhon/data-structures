def search(key, arr):
    _min, _max = 0, len(arr) - 1
    while _min <= _max:
        mid = (_max + _min) // 2
        if arr[mid] < key:
            _min = mid + 1
        elif arr[mid] > key:
            _max = mid - 1
        else:
            return mid
    return -1


inputArray = [i for i in range(100)]
print(search(5, inputArray))
print(search(101, inputArray))


def searchByRecursion(key, arr, _min, _max):
    if _min > _max:
        return -1
    mid = (_max + _min) // 2
    if arr[mid] < key:
        return searchByRecursion(key, arr, mid + 1, _max)
    elif arr[mid] > key:
        return searchByRecursion(key, arr, _min, mid - 1)
    else:
        return mid


inputArray = [i for i in range(100)]
print(searchByRecursion(5, inputArray, 0, len(inputArray) - 1))
print(searchByRecursion(101, inputArray, 0, len(inputArray) - 1))
