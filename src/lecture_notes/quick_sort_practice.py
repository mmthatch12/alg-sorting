def partition(arr):
    left = []
    pivot = arr[0]
    right = []
    for i in arr:
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return right, [pivot], left