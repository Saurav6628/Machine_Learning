import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    a=np.array(a)
    b=np.array(b)
    mag_a=np.sqrt(np.sum(a*a))
    mag_b=np.sqrt(np.sum(b*b))
    if mag_a==0 or mag_b==0:
        return 0
    dot=np.dot(a,b)
    return dot/(mag_a*mag_b)
