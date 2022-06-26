import numpy as np
import matplotlib.pyplot as plt
from create_model_base import CreateBaseModel

class CreateDstarLiteModel(CreateBaseModel):
    def __init__(self, setting):
        CreateBaseModel.__init__(self)
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

        self.adj_type = setting['adj_type']
        self.dist_type = setting['dist_type']
        self.expand_method = setting['expand_method']
        
        # successors and predecessors
        successors = [[] for i in range(self.nodes.count)]
        succ_cost = [[] for i in range(self.nodes.count)]
        predecessors = [[] for i in range(self.nodes.count)]
        pred_cost = [[] for i in range(self.nodes.count)]

        for inode in range(self.nodes.count):
            if not inode in self.obst.nodes:
                xnode = self.nodes.x[inode]
                ynode = self.nodes.y[inode]

                for iadj in range(nAdj):
                    ix = ixy[iadj][0]
                    iy = ixy[iadj][1]
                    newx = xnode+ix
                    newy = ynode+iy

                    # check if the Node is within array bound
                    if (self.map.x_min <= newx <= self.map.x_max) and (self.map.y_min <= newy <= self.map.y_max):
                        new_node = inode+ix+iy*(self.map.nx)

                        if not new_node in self.obst.nodes:
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

        self.km = 0
        self.s_last = self.robot.start_node
        self.G = np.inf*np.ones(self.nodes.count)
        self.RHS = np.inf*np.ones(self.nodes.count)


if __name__ == '__main__':
    from plot_model import plot_model
    setting = {'adj_type': '4adj', 'dist_type': 'manhattan'}
    model = CreateDstarLiteModel(setting)
    plot_model(model)
    plt.show()
