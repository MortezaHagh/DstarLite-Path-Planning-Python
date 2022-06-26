import numpy as np


def node_to_dir(model, nodes):
    dirs = []
    for i in range(1, len(nodes)):
        x1 = model.nodes.x[nodes[i-1]]
        y1 = model.nodes.y[nodes[i-1]]
        x2 = model.nodes.x[nodes[i]]
        y2 = model.nodes.y[nodes[i]]

        dy = y2-y1
        dx = x2-x1
        theta = np.arctan2(dy, dx)
        dirs.append(np.rad2deg(theta))

    dirs.append(dirs[-1])
    return dirs
