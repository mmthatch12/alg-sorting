# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for x in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        
       
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

print(selection_sort(arr1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True

            
    
    # Loop through your array
    #     Compare each element to its neighbor
    #     If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    return arr

print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr