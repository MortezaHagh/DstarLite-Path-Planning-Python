from distance import distance


class TopNode(object):
    def __init__(self, model):
        self.node = model.robot.goal_node
        self.h_cost = distance(model.robot.xs, model.robot.ys,
                               model.robot.xt, model.robot.yt, model.dist_type)
        self.key = [self.h_cost, 0]
        self.ind = 0


class Open(object):
    def __init__(self, top_node):
        self.list = [top_node]
        self.count = 1


def initialize(model):
    G = model.G
    RHS = model.RHS
    top_node = TopNode(model)
    RHS[top_node.node] = 0
    open = Open(top_node)
    return G, RHS, open
