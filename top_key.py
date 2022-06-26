import numpy as np

def top_key(open):
    
    keys = np.array([op.key for op in open.list])
    keys = keys[-1::-1][:]
    ind = np.lexsort(keys.T)
    ind = ind[-1::-1]

    top_node = open.list[ind[0]]
    top_node.ind = ind[0]

    return top_node





