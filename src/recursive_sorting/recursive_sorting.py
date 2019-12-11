# TO-DO: complete the help function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    #3. Start merging your single lists of one element together into larger, sorted sets
    for i in range(0, len(merged_arr)):
        if not arrA:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif not arrB:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] >= arrB[0]:
           merged_arr[i] = arrB[0]
           print('merged_arr', merged_arr)
           del arrB[0]
        else:
            merged_arr[i] = arrA[0]
            del arrA[0]
    print("MG return=",merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    
    if len(arr) <=1:
        return arr
    
    #1. While your data set contains more than one item, split it in half
    arrB = arr[len(arr)//2:]
    arrA = arr[:len(arr)//2]
    #2. Once you have gotten down to a single element, you have also *sorted* that element 
    #(a single element cannot be "out of order")
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    #4. Repeat step 3 until the entire data set has been reassembled
    return merge(arrA,arrB)

the = [2,5,8,1,6,0,9]

print(merge_sort(the))


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
