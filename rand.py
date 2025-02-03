"""
This module contains functions for generating random numbers, specifically
for replacing elements in an array with random values in the range 1 to 20.
"""

import secrets

def random_array(arr):
    """replaces elements in array with number in the range 1 to 20

    Args:
        arr (array): input array

    Returns:
        array : array with number in the range 1 to 20
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
