import numpy as np


def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x = np.asarray(x)
    rng = np.random.default_rng(seed=seed)
    sampled_idx = rng.integers(0, x.shape[0], size=(n_bootstrap, x.shape[0]))
    sampled_vals = x[sampled_idx]
    means = np.mean(sampled_vals, axis=1)
    mean = np.mean(means)
    alpha = (1 - ci) / 2
    quantiles = np.quantile(means, (alpha, 1 - alpha))
    return {
        "bootstrap_mean": mean,
        "lower": quantiles[0],
        "upper": quantiles[1]
    }
    