import matplotlib.pyplot as plt


def plot_model(model):
    fig, ax = plt.subplots(1, 1)
    ax.axis('equal')
    ax.axis([model.map.x_min-1, model.map.x_max+1,
            model.map.y_min-1, model.map.y_max+1])

    # start
    ax.plot(model.robot.xs, model.robot.ys, marker='^', markersize=14,
            markeredgecolor='g', markerfacecolor='g', label="Start")
    # target
    ax.plot(model.robot.xt, model.robot.yt, marker='v', markersize=14,
            markeredgecolor='r', markerfacecolor='r', label="Destination")

    # # Obstacles
    # theta = np.linspace(0, 2*np.pi, 50)
    # for i in range(0, model.obst.count):
    #     ax.fill([model.obst.x[i] + model.obst.r*np.cos(t) for t in theta],
    #             [model.obst.y[i] + model.obst.r*np.sin(t) for t in theta], 'b', edgecolor='b')
    for i in range(model.obst.count):
        ax.plot(model.obst.x, model.obst.y, 'o',  markersize=5,
                markeredgecolor='k', markerfacecolor='k')

    # Walls
    ax.plot([model.map.x_min-0.5, model.map.x_min-0.5],
            [model.map.y_min-0.5, model.map.y_max+0.5], color='k', linewidth=4)
    ax.plot([model.map.x_min-0.5, model.map.x_max+0.5],
            [model.map.y_max+0.5, model.map.y_max+0.5], color='k', linewidth=4)
    ax.plot([model.map.x_max+0.5, model.map.x_max+0.5],
            [model.map.y_max+0.5, model.map.y_min-0.5], color='k', linewidth=4)
    ax.plot([model.map.x_max+0.5, model.map.x_min-0.5],
            [model.map.y_min-0.5, model.map.y_min-0.5], color='k', linewidth=4)

    return fig, ax


if __name__ == '__main__':
    from create_model_base import CreateBaseModel
    model = CreateBaseModel()
    plot_model(model)
    plt.show()
