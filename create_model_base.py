import matplotlib.pyplot as plt


class Map(object):
    def __init__(self):
        lim = 26
        self.lim = lim
        self.x_min = 0
        self.y_min = 0
        self.x_max = lim
        self.y_max = lim
        self.nx = self.x_max - self.x_min + 1
        self.ny = self.y_max - self.y_min + 1


class Robot(object):
    def __init__(self, map):
        self.dir = 90
        self.xs = 1
        self.ys = 1
        self.xt = 7
        self.yt = 7
        self.start_node = (self.ys - map.y_min)*(map.nx) + \
            self.xs+abs(map.x_min)
        self.goal_node = (self.yt - map.y_min)*(map.nx) + \
            self.xt+abs(map.x_min)


class Obstacles(object):
    def __init__(self, map):
        self.r = 0.25
        xc1 = [3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9, 11, 11, 11]
        yc1 = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]

        xc2 = xc1*4
        yc2 = yc1 + [y+6 for y in yc1] + \
            [y+11 for y in yc1] + [y+16 for y in yc1]

        xc3 = [x+12 for x in xc2]
        yc3 = yc2

        self.x = xc2 + xc3
        self.y = yc2 + yc3

        self.count = len(self.x)
        self.nodes = [(y-map.y_min)*map.nx + x + abs(map.x_min)
                      for x, y in zip(self.x, self.y)]


class Nodes(object):
    def __init__(self, map):
        self.count = map.nx*map.ny
        self.x = [x for x in range(map.x_min, map.x_max+1)]*map.ny
        self.y = [y for y in range(map.y_min, map.y_max+1)
                  for x in range(map.nx)]


class CreateBaseModel(object):
    def __init__(self):
        print('Create Base Model')

        # Map
        map = Map()
        self.map = map

        # Robot
        self.robot = Robot(map)

        # Obstacles
        self.obst = Obstacles(map)

        # Nodes
        self.nodes = Nodes(map)


if __name__ == '__main__':
    from plot_model import plot_model
    model = CreateBaseModel()
    plot_model(model)
    plt.show()
