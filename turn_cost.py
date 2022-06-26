import numpy as np


def turn_cost(start_node, succ, model, current_dir):
    dtheta = []
    y = model.nodes.y[start_node]
    x = model.nodes.x[start_node]

    for i in succ:
        dy = model.nodes.y[i]-y
        dx = model.nodes.x[i]-x
        theta = np.arctan2(dy, dx)
        dt = np.arctan2(np.sin(theta-current_dir), np.cos(theta-current_dir))
        dtheta.append(dt)

    return dtheta
