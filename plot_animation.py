# plotAnimation1: head and tale

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class PlotAnimation1(object):

    def __init__(self, fig, ax, path):

        self.path = path
        self.ax = ax
        self.fig = fig

        self.path_len = len(path.x)

        line = [0, 0]
        line[0], = self.ax.plot(path.x[0], path.y[0], 'o',
                                markerfacecolor='green', markeredgecolor='green', markersize=5)
        line[1], = self.ax.plot(path.x[0:2], path.y
                                [0:2], color='green', linewidth=2)
        self.line = line

        self.animate()

    def ani_init(self):  # only required for blitting to give a clean slate.
        self.line[0].set_data([], [])
        self.line[1].set_data([], [])
        return self.line

    def ani_update(self, i):
        if i < self.path_len:
            x = self.path.x[i]
            y = self.path.y[i]
            self.line[0].set_data(x, y)
            xx = self.path.x[i-1:i+1]
            yy = self.path.y[i-1:i+1]
            self.line[1].set_data(xx, yy)
        return self.line

    def animate(self):
        self.anim = animation.FuncAnimation(
            self.fig, self.ani_update, init_func=self.ani_init, frames=self.path_len, repeat=False, interval=500, blit=True)
        # plt.show()
