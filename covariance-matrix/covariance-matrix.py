import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    X_avg = np.mean(X, axis=0)
    X_centered = X - X_avg
    sigma = (np.transpose(X_centered) @ X_centered) / (X_centered.shape[0] - 1)
    return sigma
    
    
    