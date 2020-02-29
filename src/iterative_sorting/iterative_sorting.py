# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # set the minimum index and iterate through the array increasing by one each time
    for min_index in range(len(arr)):

        # track the index for the minimum value
        min_value_index = min_index

        # find minium value in rest of the list min_index + 1
        for current_index in range(min_index + 1, len(arr)):
            if arr[current_index] < arr[min_value_index]:
                # store and update min_value_index
                min_value_index = current_index

        # swap the min_index and min_value_index

        arr[min_index], arr[min_value_index] = arr[min_value_index], arr[min_index]

    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr3 = [0, 1, 2, 3, 4, 5]
# print('selection sort, arr1: ', selection_sort(arr1))
# print('selection sort, arr3: ', selection_sort(arr3))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(0, n - i - 1):

            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
    # compare twe sequencial indexes i and i + 1
    # If i+1 < i, swap value and move index forward by 1
    # Repeat until no swap is made during a pass

    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]
# print('bubblesort, arr1', bubble_sort(arr1))
# print('bubblesort, arr2', bubble_sort(arr2))
# print('bubblesort, arr3', bubble_sort(arr3))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


# no negative numbers

#arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#     arr2 = []
#     arr3 = [1, 5, -2, 4, 3]

#print(count_sort(arr1))
