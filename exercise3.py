import numpy as np

def count_negatives(arr):
    """
    Counts the number of negative entries in a 1-D or 2-D NumPy array.

    Parameters:
        arr (np.ndarray): The input array, which can be 1-D or 2-D.

    Returns:
        int: The number of negative entries in the array.

    Examples:
    >>> count_negatives(np.array([1, -2, 3, -4, 5, -6]))
    3

    >>> count_negatives(np.array([[1, -1, 2], [-3, 4, -5], [6, -7, 8]]))
    4

    >>> count_negatives(np.array([10, 20, 30]))
    0

    >>> count_negatives(np.array([[-1, -2], [-3, -4]]))
    4
    """
    # Use boolean indexing to create a mask for negative values and count them


# Example usage for doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
