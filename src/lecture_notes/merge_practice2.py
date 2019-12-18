def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(0, len(merged_arr)):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]
    
    return merged_arr





def recur_merge(arr):
    if len(arr) <= 1:
        return arr
    
    arrA = arr[:len(arr)//2]
    arrB = arr[len(arr)//2:]
    arrA = recur_merge(arrA)
    arrB = recur_merge(arrB)

    return merge(arrA, arrB)

print(recur_merge([10,2,6,3,8,4]))
