# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    #loop through merged array
    for i in range(len(merged_arr)):
    #check if both elements are not empty
        if len(arrA) > 0 and len(arrB) > 0:
    #if arrA is greater than arrB
        # add arrA to merged_arr
        # remove from arrA
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
    #if arrB is greater than arrA
            else:
                merged_arr[i] = arrB.pop(0)
        # add arrB to merged_arr
        # remove from arrB

    #if arrA is empty
        # add next arrB element to merged_arr
        else:
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
    # if arrB is empty
        # add next arrB element to merged_arr
            else:
                merged_arr[i] = arrA.pop(0)

    # return merged_arr  Return statement below

    #print('length of both elements:', elements)
    #print('arrA: ', arrA)
    #print('arrB: ', arrB)
    #print("merged: ", merged_arr)
    return merged_arr


#print(merge([5, 2, 6], [3, 4, 1, 8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    arr = merge(left, right)

    return arr

#arr1 = [2, 1, 3, 5, 4]
#print(merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
