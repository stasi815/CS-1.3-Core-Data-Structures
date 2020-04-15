#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if list[index] == item:
        return index
    if index == len(list):
        return None
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, left=0, right=len(array)-1)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    #find the middle position/item
    #have a start or end (left or right)
    #check if the middle item is the target, if so return
    #else compare the target to the item in the middle
    #if target is less than ite, at the middle we ignore right half
    #if target is greater, we ignore the left half
    #repeat until target found ot we looked through everything

    # [5, 6, 7, 10, 12] item 6  - middle item is 7
    # go to middle, is the item to the right greater or less than the target

    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        if array[mid_index] == item:
            return mid_index
        #if item < array[mid_index] ignore right
        elif item < array[mid_index]:
            # change right index to
            right_index = mid_index -1
        #if item < array[mid_index] ignore right
        elif item > array[mid_index]:
            #change left index to
            left_index = mid_index + 1





def binary_search_recursive(array, item, left=None, right=None):
    mid_index = (left + right) // 2

    if array[mid_index] == item:
        return mid_index
    elif left > right:
        return None

    if array[mid_index] < item:
        return  binary_search_recursive(array, item, left + 1, right)
    if array[mid_index] > item:
        return  binary_search_recursive(array, item, left, right - 1)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
