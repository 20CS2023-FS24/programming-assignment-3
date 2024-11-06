import numpy as np

def matrix_multiply(A, B):
    """
    Perform matrix multiplication of two arrays using NumPy.
    
    Args:
        A (numpy.ndarray): First matrix of shape (m, n)
        B (numpy.ndarray): Second matrix of shape (n, p)
        
    Returns:
        numpy.ndarray: Result of matrix multiplication, shape (m, p)
        
    Raises:
        ValueError: If matrix dimensions are incompatible
        
    Examples:
    >>> import numpy as np
    >>> A = np.array([[1, 2], [3, 4]])
    >>> B = np.array([[5, 6], [7, 8]])
    >>> matrix_multiply(A, B)
    array([[19, 22],
           [43, 50]])
    
    >>> # 2x3 * 3x2 multiplication
    >>> A = np.array([[1, 2, 3], [4, 5, 6]])
    >>> B = np.array([[1, 2], [3, 4], [5, 6]])
    >>> matrix_multiply(A, B)
    array([[22, 28],
           [49, 64]])
    
    >>> # 1x2 * 2x1 multiplication (results in 1x1)
    >>> matrix_multiply(np.array([[1, 2]]), np.array([[3], [4]]))
    array([[11]])
    
    >>> # Incompatible dimensions
    >>> try:
    ...     matrix_multiply(np.array([[1, 2]]), np.array([[3, 4]]))
    ... except ValueError as e:
    ...     print("Error raised as expected")
    Error raised as expected
    
    >>> # Multiplication with identity matrix
    >>> A = np.array([[1, 2], [3, 4]])
    >>> I = np.eye(2)
    >>> np.array_equal(matrix_multiply(A, I), A)
    True
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)