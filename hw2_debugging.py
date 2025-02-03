"""implementation of merge sort"""
import rand


def merge_sort(arr):
    """performs a merge sort on the input array

    Args:
        arr (array): input arrary to sort

    Returns:
        array: sorted array
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """combines two arrays

    Args:
        left_arr (array): left array
        right_arr (array): right array

    Returns:
        array : combined array
    """
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr


input_arr = rand.random_array([None] * 20)
output_arr = merge_sort(input_arr)
print(f"input array: {input_arr}")
print(f"output array: {output_arr}")
