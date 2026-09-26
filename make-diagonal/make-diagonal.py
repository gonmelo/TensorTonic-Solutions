import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    v = np.asarray(v)
    l = len(v)
    D = np.zeros((l, l))
    for i in range(l):
        D[i,i] = v[i]
    return D