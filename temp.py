import numpy as np
import matplotlib.pyplot as plt
from create_model_base import CreateBaseModel

class CreateDstarLiteModel(CreateBaseModel):
    def __init__(self, model, setting):
        print('Create DstarLite Model from Base Model')

        if setting['adj_type'] == '4adj':
            ixy = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            nAdj = 4
        elif setting['adj_type'] == '8adj':
            ixy = [[1, 0], [0, 1], [0, -1], [-1, 0],
                   [1, 1], [-1, -1], [-1, 1], [1, -1]]
            nAdj = 8

        if setting['dist_type'] == 'manhattan':
            edge_len = 2
        elif setting['dist_type'] == 'euclidean':
            edge_len = np.sqrt(2)

        # successors and predecessors
        successors = [[]]*model.nodes.count
        succ_cost = [[]]*model.nodes.count
        predecessors = [[]]*model.nodes.count
        pred_cost = [[]]*model.nodes.count

        for inode in range(model.nodes.count):
            if not inode in model.obst.nodes:
                xnode = model.nodes.x[inode]
                ynode = model.nodes.y[inode]

                for iadj in range(nAdj):
                    ix = ixy[iadj][0]
                    iy = ixy[iadj][1]
                    newx = xnode+ix
                    newy = ynode+iy

                    # check if the Node is within array bound
                    if (model.map.x_min <= newx <= model.map.x_max) and (model.map.y_min <= newy <= model.map.y_max):
                        new_node = inode+ix+iy*(model.map.nx)

                        if not new_node in model.obst.nodes:
                            successors[inode].append(new_node)
                            predecessors[new_node].append(inode)

                            if ix != 0 and iy != 0:
                                cost = edge_len
                            else:
                                cost = 1

                            succ_cost[inode].append(cost)
                            pred_cost[new_node].append(cost)

        self.successors = successors
        self.succ_cost = succ_cost
        self.predecessors = predecessors
        self.pred_cost = pred_cost

        self.G = np.inf*np.ones(model.nodes.count)
        self.RHS = np.inf*np.ones(model.nodes.count)


if __name__ == '__main__':
    from plot_model import plot_model
    from create_model_base import CreateBaseModel
    model = CreateBaseModel()

    setting = {'adj_type': '4adj', 'dist_type': 'manhattan'}
    model_complete = CreateDstarLiteModel(model, setting)
    plot_model(model)
    plt.show()
