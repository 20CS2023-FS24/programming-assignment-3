import numpy as np

def set_negatives_to_zero(arr):
    """
    Takes a numpy array, makes a copy, and sets all negative values in the copy to 0.

    Parameters:
    arr (np.ndarray): Input array

    Returns:
    np.ndarray: A copy of the array with negative values set to 0.

    Examples:
    >>> arr = np.array([1, -2, 3, -4, 5])
    >>> set_negatives_to_zero(arr)
    array([1, 0, 3, 0, 5])

    >>> arr = np.array([-1, -2, -3, -4, -5])
    >>> set_negatives_to_zero(arr)
    array([0, 0, 0, 0, 0])

    >>> arr = np.array([0, 2, 4, 6])
    >>> set_negatives_to_zero(arr)
    array([0, 2, 4, 6])

    >>> arr = np.array([])
    >>> set_negatives_to_zero(arr)
    array([], dtype=float64)
    """
    # Make a copy of the array to avoid modifying the original
    arr_copy = arr.copy()
    # Use fancy indexing to set all negative values to 0
    arr_copy[arr_copy < 0] = 0
    return arr_copy


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)