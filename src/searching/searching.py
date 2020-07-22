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


def descending_binary_search(arr, target, start, end):
    # While the start value is <= the end value (boundary)
    while start <= end:
        # Find the midpoint
        mid = (end + start) // 2

        # Begin comparing the target to the midpoint
        if target == arr[mid]:
            return mid

        # If the target is < the midpoint
        if target < arr[mid]:
            # Cut out the left half of the array (less than) and
            # Reassign the start value to the midpoint + 1
            return descending_binary_search(arr, target, mid + 1, end)

        # If the target is > the midpoint
        if target > arr[mid]:
            # Cut out the right half of the array (greater than) and
            # Reassign the end value to the midpoint - 1
            return descending_binary_search(arr, target, start, mid - 1)


    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    # Your code here
    # Check if the input array is sorted in ascending/descending order
    # Keep a boolean to indicate the order of the array
    # Compare arr[0] and arr[1]
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if the input array is ascending, call 'binary_search' with the array and target
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # Otherwise, call the 'descending_binary_search' with the array and target
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)
