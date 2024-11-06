import numpy as np

def custom_matrix(n, a, b, c):
    """
    Creates an n x n matrix where:
    - Diagonal entries are set to `a`
    - Entries above the diagonal are set to `b`
    - Entries below the diagonal are set to `c`

    Parameters:
    n (int): Size of the matrix (n x n).
    a (int): Value for the diagonal elements.
    b (int): Value for the elements above the diagonal.
    c (int): Value for the elements below the diagonal.

    Returns:
    np.ndarray: The resulting n x n matrix.

    Examples:
    >>> np.array_equal(custom_matrix(3, 1, -1, 2), np.array([
    ...     [ 1, -1, -1],
    ...     [ 2,  1, -1],
    ...     [ 2,  2,  1]
    ... ]))
    True

    >>> np.array_equal(custom_matrix(4, 5, 10, -5), np.array([
    ...     [ 5, 10, 10, 10],
    ...     [-5,  5, 10, 10],
    ...     [-5, -5,  5, 10],
    ...     [-5, -5, -5,  5]
    ... ]))
    True

    >>> np.array_equal(custom_matrix(2, 7, -3, 4), np.array([
    ...     [ 7, -3],
    ...     [ 4,  7]
    ... ]))
    True

    >>> np.array_equal(custom_matrix(5, 4, -7, 2), np.array([
    ...     [ 4, -7, -7, -7, -7],
    ...     [ 2,  4, -7, -7, -7],
    ...     [ 2,  2,  4, -7, -7],
    ...     [ 2,  2,  2,  4, -7],
    ...     [ 2,  2,  2,  2,  4]
    ... ]))
    True
    """
    pass

# Example usage
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
