import numpy as np
from turn_cost import turn_cost
from initialize import initialize
from update_map import update_map
from node_to_dir import node_to_dir
from compute_shortest_path import compute_shortest_path


class Start(object):
    def __init__(self, model, G, RHS):
        self.node = model.robot.start_node
        self.key = [min(G[self.node], RHS[self.node])]*2
        self.x = model.nodes.x[self.node]
        self.y = model.nodes.y[self.node]


class Path(object):
    def __init__(self, model, path_nodes):
        self.nodes = path_nodes
        self.x = [model.nodes.x[i] for i in path_nodes]
        self.y = [model.nodes.y[i] for i in path_nodes]
        self.dirs = node_to_dir(model, path_nodes)


def dstar_lite(model):

    [G, RHS, open] = initialize(model)

    t = 1
    current_dir = np.deg2rad(model.robot.dir)
    path_nodes = [model.robot.start_node]

    # start
    start = Start(model, G, RHS)

    # compute shortest path
    [G, RHS, open, start] = compute_shortest_path(G, RHS, open, start, model)

    # # main procedure
    while start.node != model.robot.goal_node:

        # move robot to next node
        succ = model.successors[start.node]
        succ_c = np.array(model.succ_cost[start.node])
        succ_g = np.array(G[succ])
        if model.expand_method == 'random':
            min_ind = np.argmin(succ_c+succ_g)
            start.node = succ[min_ind]
        elif model.expand_method == 'heading':
            dtheta = turn_cost(start.node, succ, model, current_dir)
            c1 = succ_c+succ_g
            c2 = [np.abs(dtheta), c1]
            c3 = np.array(c2)
            inds = np.lexsort(c3)
            start.node = succ[inds[0]]
            current_dir = current_dir + dtheta[inds[0]]

        start.x = model.nodes.x[start.node]
        start.y = model.nodes.y[start.node]

        # move to start.node and add start.node to Path
        t = t+1
        path_nodes.append(start.node)

        # # check for update in edge costs (obstacles)
        # [open, RHS, model] = update_map(open, RHS, G, model, start, t)

        # compute shortest path
        [G, RHS, open, start] = compute_shortest_path(
            G, RHS, open, start, model)

    path = Path(model, path_nodes)

    return model, path
