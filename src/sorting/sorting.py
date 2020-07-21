# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here

    # Set a and b's values to be the length
    # of their respective arrays
    a = len(arrA)
    b = len(arrB)
    # Set the index of a and b to 0 (starting)
    a_ndx = 0
    b_ndx = 0
    # Set count to 0 (starting)
    count = 0

    # While both arrays' indices are less than their respective lengths...
    while(a_ndx < a and b_ndx < b):
        # Add one to the count
        count += 1
        
        # During this iteration of the loop,
        # if array A at this index is less than array B at this index...
        if arrA[a_ndx] < arrB[b_ndx]:
            # Append this element to the merged_arr
            merged_arr.append(arrA[a_ndx])
            # Add one to the A index
            a_ndx += 1
        # Otherwise...
        else:
            # Append this element to the merged_arr
            merged_arr.append(arrB[b_ndx])
            # Add one to the B index
            b_ndx += 1

    # Return the merged array plus both altered arrays
    return merged_arr + arrA[a_ndx:] + arrB[b_ndx:]

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # Base case
    # If the length of the array is <= 1, return array
    if len(arr) <= 1:
        return arr
    else:
        # Find the middle of the array
        mid = len(arr)//2
        # Set arrA to be everything to the left of the mid
        arrA = arr[:mid]
        # Set arrB to be everything to the right of the mid
        arrB = arr[mid:]
        # Run this function recursively to sort the arrays for the merge function
        return merge(merge_sort(arrA), merge_sort(arrB))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

