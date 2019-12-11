def helper_merge(arA, arB):
    elements = len(arA) + len(arB)
    empty = [0] * elements
    for i in range(0, len(empty)):
        if not arA:
            empty[i] = arB[0]
            del arB[0]
        elif not arB:
            empty[i] = arA[0]
            del arA[0]
        elif arA[0] >= arB[0]:
            empty[i] = arB[0]
            del arB[0]
        else:
            empty[i] = arA[0]
            del arA[0]
    return empty


def recur_merger(arr):
    if len(arr) <= 1:
        return arr
    arA = arr[:len(arr)//2]
    arB = arr[len(arr)//2:]
    arA = recur_merger(arA)
    arB = recur_merger(arB)

    return helper_merge(arA, arB)

print(recur_merger([70,6,52,51,80,0,8,21,23,23]))