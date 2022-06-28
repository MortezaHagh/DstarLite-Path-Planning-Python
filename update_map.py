import numpy as np
from distance import distance
from update_vertex import update_vertex


def update_map(open, RHS, G, model, start, t):

    if t == 2:
        new_obst_node = 31
        for ind, node in enumerate(model.predecessors[new_obst_node]):
            model.pred_cost[new_obst_node][ind] = np.inf
            suc_ind = np.where(new_obst_node==model.successors[node])
            model.succ_cost[node][suc_ind] = np.inf

        xl = model.nodes.x[model.s_last]
        yl = model.nodes.y[model.s_last]
        model.km = model.km + \
            distance(xl, yl, start.x, start.y, model.dist_type)
        model.s_last = start.node
        update_list = model.predecessors[new_obst_node]

        # update vertex
        [open, RHS] = update_vertex(open, RHS, G, update_list, model, start)

    return open, RHS, model
