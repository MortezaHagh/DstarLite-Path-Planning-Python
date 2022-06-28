import numpy as np


def top_key(open):

    keys = np.array([[np.random.rand(1)[-1], op.key[1], op.key[0]]
                    for op in open.list])
    ind = np.lexsort(keys.T)
    top_node = open.list[ind[0]]
    top_node.ind = ind[0]

    return top_node
