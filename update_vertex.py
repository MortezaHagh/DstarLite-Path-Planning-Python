import numpy as np
from distance import distance
from initialize import TopNode


def update_vertex(open, RHS, G, update_list, model, start):
    for inode in update_list:
        if inode != model.robot.goal_node:
            succ = model.successors[inode]
            succ_c = model.succ_cost[inode]
            succ_g = np.array(G[succ])
            RHS[inode] = min(succ_g+succ_c)

        open_nodes = [op.node for op in open.list]
        if inode in open_nodes:
            ind = open_nodes.index(inode)
            open.list.pop(ind)
            open.count -= 1

        if G[inode] != RHS[inode]:
            open.count += 1
            op = TopNode(model)
            op.node = inode
            x = model.nodes.x[inode]
            y = model.nodes.y[inode]
            op.h_cost = distance(start.x, start.y, x, y, model.dist_type)
            c = min(G[inode], RHS[inode])
            op.key = [c+model.km+op.h_cost, c]
            op.ind = open.count
            open.list.append(op)

    return open, RHS
