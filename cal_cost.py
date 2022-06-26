import numpy as np


def cal_cost(path):

    dxPath = np.diff(path.x)
    dyPath = np.diff(path.y)
    dxPath2 = np.power(dxPath, 2)
    dyPath2 = np.power(dyPath, 2)

    # path length
    path_length = sum(np.sqrt(np.add(dxPath2, dyPath2)))

    return path_length
