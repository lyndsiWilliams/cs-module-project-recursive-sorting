# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # While the start value is <= the end value (boundary)
    while start <= end:
        # Find the midpoint
        mid = (end + start) // 2

        # Begin comparing the target to the midpoint
        if target == arr[mid]:
            return mid

        # If the target is < the midpoint
        if target < arr[mid]:
            # Cut out the right half of the array (greater than) and
            # Reassign the end value to the midpoint - 1
            return binary_search(arr, target, start, mid - 1)

        # If the target is > the midpoint
        if target > arr[mid]:
            # Cut out the left half of the array (less than) and
            # Reassign the start value to the midpoint + 1
            return binary_search(arr, target, mid + 1, end)


    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

