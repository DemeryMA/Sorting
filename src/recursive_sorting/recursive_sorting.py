arr = [9, 7, 16, 32, 55, 84, 97, 63, 62, 1]
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    
    return merged_arr

# U merge two arrays
# P Take two arrays and combine them as their combining were going to sort them from least to greatest between the two
# E
# R


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr 
    # Divide in half
    left = arr[ : len(arr) // 2]
    right = arr[len(arr) // 2: ]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)


print(merge_sort(arr))

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
