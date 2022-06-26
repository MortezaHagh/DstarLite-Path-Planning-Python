import numpy as np
from top_key import top_key
from compare_keys import compare_keys
from update_vertex import update_vertex


def compute_shortest_path(G, RHS, open, start, model):

    # select top key
    top_node = top_key(open)

    # update start_key
    c = min(G[start.node], RHS[start.node])
    start.key = [c+model.km, c]

    while compare_keys(top_node.key, start.key) or RHS[start.node] != G[start.node]:
        k_old = top_node.key
        k_new = min(G[top_node.node], RHS[top_node.node]) + \
            np.array([top_node.h_cost+model.km, 0])

        # remove topkey from open
        open.list.pop(top_node.ind)
        open.count = open.count - 1

        # update vertex
        update_list = model.predecessors[top_node.node]
        if compare_keys(k_old, k_new):
            open.list.append(top_node)
            open.list[-1].key = k_new
            open.count += 1
        else:
            if G[top_node.node] > RHS[top_node.node]:
                G[top_node.node] = RHS[top_node.node]
            else:
                G[top_node.node] = np.inf
                update_list.append(top_node.node)
            [open, RHS] = update_vertex(
                open, RHS, G, update_list, model, start)

        # select top key
        top_node = top_key(open)

        # update start_key
        c = min(G[start.node], RHS[start.node])
        start.key = [c+model.km, c]

    return G, RHS, open, start
