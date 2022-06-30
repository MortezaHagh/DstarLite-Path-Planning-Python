import numpy as np


def cal_smoothness(path):

    nodes = path.nodes
    dirs = path.dirs
    dn = np.diff(nodes)
    dirs1 = np.array(dirs)
    dirs1 = np.deg2rad(dirs1)
    dirs2 = dirs1[np.where(dn != 0)]
    d_theta = [np.arctan2(np.sin(dirs2[i]-dirs2[i-1]),
                          np.cos(dirs2[i]-dirs2[i-1])) for i in range(1, len(dirs2))]
    d_theta = sum(np.abs(d_theta))
    smoothness = np.rad2deg(d_theta)

    return smoothness
