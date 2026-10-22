import numpy as np


def matmul_from_scratch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ans=np.zeros((a.shape[0],b.shape[1]))
    if a.shape[1]!=b.shape[0]:
        raise ValueError
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                ans[i][j]+=a[i][k]*b[k][j]
    return ans
