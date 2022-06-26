import numpy as np

def cal_smoothness(path):
    dtheta = np.diff(path.dirs)
    smoothness = sum(abs(dtheta))
    return smoothness
