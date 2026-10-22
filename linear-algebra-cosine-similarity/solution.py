import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    # TODO: Dot product divided by the product of the norms.
    mag_a=np.sqrt(np.sum(a*a))
    mag_b=np.sqrt(np.sum(b*b))
    if mag_a==0 or mag_b==0:
        return 0
    dot=np.dot(a,b)
    return dot/(mag_a*mag_b)
